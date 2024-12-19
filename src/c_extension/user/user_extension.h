#ifndef USER_H
#define USER_H

typedef struct {
    int id;
    char username[50];
    char firstname[50];
    char lastname[50];
    int birth_date;
} CUser;

typedef struct {
    char firstname[50];
    char lastname[50];
    float avg_rating;
} Director;

typedef struct {
    char name[50];
    float avg_rating;
} Genre;

typedef struct {
    char title[50];
    int rating;
    int sale_date;
} MinimizedUserMovie;

typedef struct {
    int user_id;
    Director directors[3];
    Genre genres[3];
    MinimizedUserMovie user_movies[100];
    int movie_count;
} UserProfile;

CUser get(char* db_directory, char* username);

UserProfile get_user_profile(char* db_directory, int user_id);

#endif /* USER_H */
