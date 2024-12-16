#ifndef USER_H
#define USER_H

typedef struct {
    int id;
    char username[50];
    char firstname[50];
    char lastname[50];
    int birth_date;
} CUser;

CUser _get(char* db_directory, char* username);

int _test(char* db_directory, int id);

#endif /* USER_H */
