#include <stdio.h>
#include <sqlite3.h>
#include <stdlib.h>

// Fonction pour calculer la similarité de Jaccard
float calculer_jaccard(sqlite3 *db, int user1_id, int user2_id) {
    sqlite3_stmt *stmt;
    int intersection = 0;
    int union_taille = 0;

    // Requête pour calculer l'intersection
    const char *query_intersection = 
        "SELECT COUNT(*) "
        "FROM user_movies AS um1 "
        "JOIN user_movies AS um2 "
        "ON um1.movie_id = um2.movie_id "
        "WHERE um1.user_id = ? AND um2.user_id = ?;";
    
    // Préparation et exécution de la requête pour l'intersection
    sqlite3_prepare_v2(db, query_intersection, -1, &stmt, NULL);
    sqlite3_bind_int(stmt, 1, user1_id);
    sqlite3_bind_int(stmt, 2, user2_id);

    if (sqlite3_step(stmt) == SQLITE_ROW) {
        intersection = sqlite3_column_int(stmt, 0);
    }
    sqlite3_finalize(stmt);

    // Impression des résultats de l'intersection
    printf("Résultat de l'intersection : %d\n", intersection);

    // Requête pour calculer l'union
    const char *query_union = 
        "SELECT COUNT(DISTINCT movie_id) "
        "FROM user_movies "
        "WHERE user_id = ? OR user_id = ?;";

    // Préparation et exécution de la requête pour l'union
    sqlite3_prepare_v2(db, query_union, -1, &stmt, NULL);
    sqlite3_bind_int(stmt, 1, user1_id);
    sqlite3_bind_int(stmt, 2, user2_id);

    if (sqlite3_step(stmt) == SQLITE_ROW) {
        union_taille = sqlite3_column_int(stmt, 0);
    }
    sqlite3_finalize(stmt);

    // Impression des résultats de l'union
    printf("Résultat de l'union : %d\n", union_taille);

    // Calcul de la similarité
    if (union_taille == 0) {
        return 0.0; // Éviter la division par zéro
    }
    return (float)intersection / union_taille;
}

int main() {
    sqlite3 *db;
    int rc = sqlite3_open("films_recommendation.db", &db);

    if (rc) {
        fprintf(stderr, "Erreur d'ouverture de la base de données : %s\n", sqlite3_errmsg(db));
        return 1;
    }

    int user1_id = 1;
    int user2_id = 2;

    float similarite = calculer_jaccard(db, user1_id, user2_id);

    printf("La similarité de Jaccard entre l'utilisateur %d et l'utilisateur %d est : %.2f\n", 
            user1_id, user2_id, similarite);

    sqlite3_close(db);
    return 0;
}
