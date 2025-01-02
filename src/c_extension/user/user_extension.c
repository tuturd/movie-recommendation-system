#include <stdio.h>
#include <sqlite3.h>
#include <string.h>
#include "user_extension.h"

/**
 * @brief Récupère un utilisateur de la base de données.
 * 
 * Cette fonction prend en entrée un identifiant d'utilisateur et retourne un objet CUser correspondant à cet identifiant.
 * 
 * @param db_directory Chemin vers le fichier de la base de données SQLite.
 * @param user_id ID de l'utilisateur à récupérer.
 * @return CUser Retourne un objet CUser contenant les informations de l'utilisateur.
 * 
 * @example
 * CUser user = get_user("users.db", 1);
 * printf("Nom: %s, Email: %s\n", user.name, user.email);
 */

CUser get(char* db_directory, char* username) {
    sqlite3 *db;
    sqlite3_stmt *stmt;
    int result_count = 0;

    int rc = sqlite3_open(db_directory, &db);

    if (rc) {
        fprintf(stderr, "Erreur d'ouverture de la base de données : %s\n", sqlite3_errmsg(db));
        return;
    }

    // Requête pour obtenir tous les autres utilisateurs
    const char *query_users =
        "SELECT id, username, firstname, lastname, birthDate FROM user WHERE username = ?;";

    sqlite3_prepare_v2(db, query_users, -1, &stmt, NULL);
    sqlite3_bind_text(stmt, 1, username, -1, SQLITE_STATIC);

    CUser user;
    while (sqlite3_step(stmt) == SQLITE_ROW) {
        user.id = sqlite3_column_int(stmt, 0);
        strncpy(user.username, (const char*)sqlite3_column_text(stmt, 1), sizeof(user.username) - 1);
        user.username[sizeof(user.username) - 1] = '\0';
        strncpy(user.firstname, (const char*)sqlite3_column_text(stmt, 2), sizeof(user.firstname) - 1);
        user.firstname[sizeof(user.firstname) - 1] = '\0';
        strncpy(user.lastname, (const char*)sqlite3_column_text(stmt, 3), sizeof(user.lastname) - 1);
        user.lastname[sizeof(user.lastname) - 1] = '\0';
        user.birth_date = sqlite3_column_int(stmt, 4);
    }

    sqlite3_finalize(stmt);
    sqlite3_close(db);

    return user;
}

/**
 * @brief Récupère le profil d'un utilisateur à partir de la base de données.
 * 
 * Cette fonction interroge la base de données SQLite pour obtenir les informations de profil complet d'un utilisateur spécifique en utilisant son ID.
 * 
 * @param db_directory Chemin vers le fichier de la base de données SQLite.
 * @param user_id ID de l'utilisateur dont le profil doit être récupéré.
 * @return UserProfile Retourne une structure UserProfile contenant les informations de l'utilisateur.
 * 
 * @example
 * UserProfile profile = get_user_profile("app.db", 1);
 * printf("Nom: %s, Âge: %d\n", profile.name, profile.age);
 */

UserProfile get_user_profile(char* db_directory, int user_id) {
    sqlite3 *db;
    sqlite3_stmt *stmt;
    UserProfile user_profile;
    int count = 0;

    int rc = sqlite3_open(db_directory, &db);

    if (rc) {
        fprintf(stderr, "Erreur d'ouverture de la base de données : %s\n", sqlite3_errmsg(db));
        return;
    }

    const char *query_users = 
        "SELECT rating, saleDate, m.title FROM userMovie um JOIN movie m ON um.movieId = m.id WHERE userId = ? LIMIT 100;";

    sqlite3_prepare_v2(db, query_users, -1, &stmt, NULL);
    sqlite3_bind_int(stmt, 1, user_id);

    while (sqlite3_step(stmt) == SQLITE_ROW) {
        MinimizedUserMovie movie;
        movie.rating = sqlite3_column_int(stmt, 0);
        movie.sale_date = sqlite3_column_int(stmt, 1);
        strncpy(movie.title, (const char*)sqlite3_column_text(stmt, 2), sizeof(movie.title) - 1);
        movie.title[sizeof(movie.title) - 1] = '\0';
        user_profile.user_movies[count++] = movie;
    }
    user_profile.movie_count = count;

    const char *query_directors = 
        "SELECT d.firstname, d.lastname, AVG(um.rating) as avg_rating FROM userMovie um JOIN movie m ON um.movieId = m.id JOIN director d ON m.directorId = d.id WHERE um.userId = ? GROUP BY d.id ORDER BY avg_rating DESC LIMIT 3;";

    sqlite3_prepare_v2(db, query_directors, -1, &stmt, NULL);
    sqlite3_bind_int(stmt, 1, user_id);

    count = 0;
    while (sqlite3_step(stmt) == SQLITE_ROW && count < 3) {
        Director director;
        strncpy(user_profile.directors[count].firstname, (const char*)sqlite3_column_text(stmt, 0), sizeof(user_profile.directors[count].firstname) - 1);
        user_profile.directors[count].firstname[sizeof(user_profile.directors[count].firstname) - 1] = '\0';
        strncpy(user_profile.directors[count].lastname, (const char*)sqlite3_column_text(stmt, 1), sizeof(user_profile.directors[count].lastname) - 1);
        user_profile.directors[count].lastname[sizeof(user_profile.directors[count].lastname) - 1] = '\0';
        user_profile.directors[count].avg_rating = sqlite3_column_double(stmt, 2);
        count++;
    }

    const char *query_genres = 
        "SELECT g.name, AVG(um.rating) as avg_rating FROM userMovie um JOIN movie m ON um.movieId = m.id JOIN genre g ON m.genreId = g.id WHERE um.userId = ? GROUP BY g.id ORDER BY avg_rating DESC LIMIT 3;";

    sqlite3_prepare_v2(db, query_genres, -1, &stmt, NULL);
    sqlite3_bind_int(stmt, 1, user_id);

    count = 0;
    while (sqlite3_step(stmt) == SQLITE_ROW && count < 3) {
        
        strncpy(user_profile.genres[count].name, (const char*)sqlite3_column_text(stmt, 0), sizeof(user_profile.genres[count].name) - 1);
        user_profile.genres[count].name[sizeof(user_profile.genres[count].name) - 1] = '\0';
        user_profile.genres[count].avg_rating = sqlite3_column_double(stmt, 1);
        printf("%s\n", user_profile.genres[count].name);
        printf("%f\n", user_profile.genres[count].avg_rating);
        count++;
    }

    sqlite3_finalize(stmt);
    sqlite3_close(db);

    return user_profile;
}