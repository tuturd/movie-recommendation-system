#include <stdio.h>
#include <sqlite3.h>
#include <string.h>
#include "user_extension.h"

CUser _get(char* db_directory, char* username) {
    sqlite3 *db;
    sqlite3_stmt *stmt;
    int result_count = 0;
    char sql[256];

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

int _test(char* db_directory, int id) {
    sqlite3 *db;
    sqlite3_stmt *stmt;
    char *err_msg = 0;
    int rc;
    char sql[256];

    rc = sqlite3_open(db_directory, &db);

    if (rc != SQLITE_OK) {
        fprintf(stderr, "Cannot open database: %s\n", sqlite3_errmsg(db));
        return;
    }

    snprintf(sql, sizeof(sql), "SELECT * FROM User WHERE id = 1;", id);
    // snprintf(sql, sizeof(sql), "SELECT * FROM User WHERE id = '%d';", id);

    rc = sqlite3_prepare_v2(db, sql, -1, &stmt, 0);

    if (rc != SQLITE_OK) {
        fprintf(stderr, "Failed to execute statement: %s\n", sqlite3_errmsg(db));
        sqlite3_close(db);
        return;
    }

    CUser user;
    user.id = sqlite3_column_int(stmt, 0);
    printf("ID : %d\n", user.id);
    strncpy(user.username, (const char*)sqlite3_column_text(stmt, 1), sizeof(user.username) - 1);
    user.username[sizeof(user.username) - 1] = '\0';
    strncpy(user.firstname, (const char*)sqlite3_column_text(stmt, 2), sizeof(user.firstname) - 1);
    user.firstname[sizeof(user.firstname) - 1] = '\0';
    strncpy(user.lastname, (const char*)sqlite3_column_text(stmt, 3), sizeof(user.lastname) - 1);
    user.lastname[sizeof(user.lastname) - 1] = '\0';
    user.birth_date = sqlite3_column_int(stmt, 4);

    sqlite3_finalize(stmt);
    sqlite3_close(db);

    return user.id;
}