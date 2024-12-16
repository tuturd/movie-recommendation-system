#include <sqlite3.h>

// Structure pour stocker les résultats de similarité
typedef struct {
    int user_id;      // ID de l'autre utilisateur
    float similarite; // Résultat de la similarité de Jaccard
} ResultatSimilarite;

float calculer_jaccard(sqlite3 *db, int user1_id, int user2_id);

ResultatSimilarite* calculer_similarites_pour_utilisateur(char *db_directory, int target_user_id);