import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Chemin vers la base de données
DB_NAME = "../database/seed/seed.db"

# Connexion à la base de données
def connect_to_db():
    return sqlite3.connect(DB_NAME)

# Ajouter une vente
def ajouter_vente(user_id, movie_id):
    conn = connect_to_db()
    cursor = conn.cursor()

    # Vérifier si le film existe
    cursor.execute("SELECT title FROM movie WHERE id = ?", (movie_id,))
    film = cursor.fetchone()

    if not film:
        print("Erreur : Film introuvable.")
        conn.close()
        return

    title = film[0]
    sale_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Ajouter la vente
    cursor.execute(
        "INSERT INTO userMovie (userId, movieId, rating, sold, saleDate) VALUES (?, ?, ?, ?, ?)",
        (user_id, movie_id, 5, 1, sale_date)
    )
    conn.commit()
    conn.close()
    print(f"Vente ajoutée : {title} pour l'utilisateur {user_id}.")

# Exporter les ventes en CSV
def exporter_ventes():
    conn = connect_to_db()
    query = """
    SELECT u.firstname || ' ' || u.lastname AS Utilisateur, 
           m.title AS Film, 
           um.saleDate AS Date_Vente
    FROM userMovie um
    JOIN user u ON um.userId = u.id
    JOIN movie m ON um.movieId = m.id
    WHERE um.sold = 1;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()

    if df.empty:
        print("Aucune vente enregistrée.")
        return

    # Chemin d'enregistrement
    file_path = input("Entrez le chemin pour enregistrer le fichier CSV : ")
    df.to_csv(file_path, index=False)
    print(f"Les ventes ont été exportées dans : {file_path}")

# Volume des ventes des 6 derniers mois
def volume_6_mois():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    SELECT strftime('%Y-%m', saleDate) AS mois, COUNT(*) AS volume
    FROM userMovie
    WHERE saleDate >= date('now', '-6 months') AND sold = 1
    GROUP BY mois
    ORDER BY mois ASC;
    """
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()

    if not data:
        print("Aucune vente enregistrée dans les 6 derniers mois.")
        return

    mois = [row[0] for row in data]
    volumes = [row[1] for row in data]

    plt.switch_backend('TkAgg')
    plt.figure(figsize=(10, 5))
    plt.bar(mois, volumes, color='skyblue')
    plt.title("Volume des ventes des 6 derniers mois")
    plt.xlabel("Mois")
    plt.ylabel("Nombre de ventes")
    plt.tight_layout()
    plt.show()

# Top 3 des utilisateurs ayant consommé le plus
def top_3_utilisateurs():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    SELECT u.username, COUNT(*) AS total_achats
    FROM userMovie um
    JOIN user u ON um.userId = u.id
    WHERE um.sold = 1
    GROUP BY um.userId
    ORDER BY total_achats DESC
    LIMIT 3;
    """
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()

    if not data:
        print("Aucune vente enregistrée.")
        return

    utilisateurs = [row[0] for row in data]
    volumes = [row[1] for row in data]

    plt.switch_backend('TkAgg')
    plt.figure(figsize=(7, 7))
    plt.pie(volumes, labels=utilisateurs, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightcoral', 'lightskyblue'])
    plt.title("Top 3 des utilisateurs ayant consommé le plus")
    plt.tight_layout()
    plt.show()

# Top 5 des films les plus vendus
def top_5_films():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    SELECT m.title, COUNT(*) AS ventes
    FROM userMovie um
    JOIN movie m ON um.movieId = m.id
    WHERE um.sold = 1
    GROUP BY um.movieId
    ORDER BY ventes DESC
    LIMIT 5;
    """
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()

    if not data:
        print("Aucun film vendu.")
        return

    films = [row[0] for row in data]
    ventes = [row[1] for row in data]

    plt.switch_backend('TkAgg')
    plt.figure(figsize=(10, 5))
    plt.bar(films, ventes, color='lightgreen')
    plt.title("Top 5 des films les plus vendus")
    plt.xlabel("Films")
    plt.ylabel("Nombre de ventes")
    plt.tight_layout()
    plt.show()