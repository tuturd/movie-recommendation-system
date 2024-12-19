#include <stdio.h>
#include <sqlite3.h>
#include <stdlib.h>

// Structure pour stocker les résultats de similarité
typedef struct {
    int user_id;      // ID de l'autre utilisateur
    float similarite; // Résultat de la similarité de Jaccard
} ResultatSimilarite;

// Fonction pour calculer la similarité de Jaccard entre deux utilisateurs
float calculer_jaccard(sqlite3 *db, int user1_id, int user2_id) {
    sqlite3_stmt *stmt;
    int intersection = 0;
    int union_taille = 0;

    // Requête pour calculer l'intersection
    const char *query_intersection =
        "SELECT COUNT(*) "
        "FROM userMovie AS um1 "
        "JOIN userMovie AS um2 "
        "ON um1.movieId = um2.movieId "
        "WHERE um1.userId = ? AND um2.userId = ?;";
        "FROM userMovie AS um1 "
        "JOIN userMovie AS um2 "
        "ON um1.movieId = um2.movieId "
        "WHERE um1.userId = ? AND um2.userId = ?;";

    sqlite3_prepare_v2(db, query_intersection, -1, &stmt, NULL);
    sqlite3_bind_int(stmt, 1, user1_id);
    sqlite3_bind_int(stmt, 2, user2_id);

    if (sqlite3_step(stmt) == SQLITE_ROW) {
        intersection = sqlite3_column_int(stmt, 0);
    }
    sqlite3_finalize(stmt);

    // Requête pour calculer l'union
    const char *query_union =
        "SELECT COUNT(DISTINCT movieId) "
        "FROM userMovie "
        "WHERE userId = ? OR userId = ?;";

    sqlite3_prepare_v2(db, query_union, -1, &stmt, NULL);
    sqlite3_bind_int(stmt, 1, user1_id);
    sqlite3_bind_int(stmt, 2, user2_id);

    if (sqlite3_step(stmt) == SQLITE_ROW) {
        union_taille = sqlite3_column_int(stmt, 0);
    }
    sqlite3_finalize(stmt);

    if (union_taille == 0) {
        return 0.0;
    }
    return (float)intersection / union_taille;
}

// Fonction pour calculer les similarités pour un utilisateur donné
ResultatSimilarite* calculer_similarites_pour_utilisateur(char *db_directory, int target_user_id) {
    sqlite3 *db;
    sqlite3_stmt *stmt;
    ResultatSimilarite *results = NULL;
    int result_count = 0;

    int rc = sqlite3_open(db_directory, &db);

    if (rc) {
        fprintf(stderr, "Erreur d'ouverture de la base de données : %s\n", sqlite3_errmsg(db));
        exit(EXIT_FAILURE);
        return NULL;
    }

    const char *query_users = "SELECT id FROM user WHERE id != ?;";

    sqlite3_prepare_v2(db, query_users, -1, &stmt, NULL);
    sqlite3_bind_int(stmt, 1, target_user_id);

    while (sqlite3_step(stmt) == SQLITE_ROW) {
        int user_id = sqlite3_column_int(stmt, 0);

        // Recalculer la taille et allouer un nouvel espace pour les résultats
        results = realloc(results, (result_count + 1) * sizeof(ResultatSimilarite));
        if (!results) {
            fprintf(stderr, "Erreur d'allocation mémoire\n");
            exit(EXIT_FAILURE);
        }

        // Stocker l'ID de l'utilisateur et la similarité calculée
        results[result_count].user_id = user_id;
        results[result_count].similarite = calculer_jaccard(db, target_user_id, user_id);
        result_count++;
    }
    sqlite3_finalize(stmt);
    sqlite3_close(db);

    results = realloc(results, (result_count + 1) * sizeof(ResultatSimilarite));
    if (!results) {
        fprintf(stderr, "Erreur d'allocation mémoire\n");
        exit(EXIT_FAILURE);
    }
    results[result_count].user_id = -1;
    results[result_count].similarite = 0;

    return results;
}



int main() {
    // sqlite3 *db;
    // int rc = sqlite3_open("films_recommendation.db", &db);

    // if (rc) {
    //     fprintf(stderr, "Erreur d'ouverture de la base de données : %s\n", sqlite3_errmsg(db));
    //     return 1;
    // }

    // int target_user_id = 1; // ID de l'utilisateur pour lequel on calcule les similarités
    // int result_count = 0;

    // // Calcul des similarités
    // ResultatSimilarite *similarites = calculer_similarites_pour_utilisateur(db, target_user_id, &result_count);

    // // Affichage des résultats
    // printf("Similarités de Jaccard pour l'utilisateur %d :\n", target_user_id);
    // for (int i = 0; i < result_count; i++) {
    //     printf("Utilisateur %d : Similarité = %.2f\n",
    //            similarites[i].user_id, similarites[i].similarite);
    // }

    // // Libération de la mémoire
    // free(similarites);

    // sqlite3_close(db);
    // return 0;
}
