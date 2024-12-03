#include <stdio.h>
#include <sqlite3.h>
#include "double_extension.h"

int double_value(int x) {
    return (x * 2);
}

void execute_sql_query(char* db_directory, char* username) {
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

    snprintf(sql, sizeof(sql), "SELECT * FROM User WHERE username = '%s';", username);

    rc = sqlite3_prepare_v2(db, sql, -1, &stmt, 0);

    if (rc != SQLITE_OK) {
        fprintf(stderr, "Failed to execute statement: %s\n", sqlite3_errmsg(db));
        sqlite3_close(db);
        return;
    }

    while (sqlite3_step(stmt) == SQLITE_ROW) {
        printf("User ID: %d\n", sqlite3_column_int(stmt, 0));
        printf("username: %s\n", sqlite3_column_text(stmt, 1));
        // Add more columns as needed
    }

    sqlite3_finalize(stmt);
    sqlite3_close(db);
}