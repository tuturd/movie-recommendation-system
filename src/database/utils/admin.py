import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import src.database.utils.connection as db
from src.utils.logging import get_logger

logger = get_logger(__name__)


# Ajouter une vente
def ajouter_vente(user_id, movie_id):
    """
    Ajoute une vente pour un utilisateur et un film donnés.

    Parameters:
    -----------
    user_id : int
        L'identifiant de l'utilisateur.
    movie_id : int
        L'identifiant du film.

    Raises:
    -------
    UserMovieError
        Si une erreur opérationnelle se produit lors du processus d'insertion.
    """

    conn = db.open_connection()
    cursor = conn.cursor()

    # Vérifier si le film existe
    cursor.execute('SELECT title FROM movie WHERE id = ?', (movie_id,))
    film = cursor.fetchone()

    if not film:
        logger.error('Erreur : Film introuvable.')
        conn.close()
        return

    title = film[0]
    sale_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Ajouter la vente
    cursor.execute(
        'INSERT INTO userMovie (userId, movieId, rating, sold, saleDate) VALUES (?, ?, ?, ?, ?)',
        (user_id, movie_id, 5, 1, sale_date)
    )
    conn.commit()
    conn.close()
    logger.info(f"Vente ajoutée : {title} pour l'utilisateur {user_id}.")


# Exporter les ventes en CSV
def exporter_ventes():
    """
    Exports sales data to a CSV file.
    This function retrieves sales data from the database, including user names,
    movie titles, and sale dates, and exports it to a CSV file specified by the user.
    """

    conn = db.open_connection()
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
        logger.warning('Aucune vente enregistrée.')
        return

    # Chemin d'enregistrement
    file_path = input('Entrez le chemin pour enregistrer le fichier CSV : ')
    df.to_csv(file_path, index=False)
    logger.info(f'Les ventes ont été exportées dans : {file_path}')


# Volume des ventes des 6 derniers mois
def volume_6_mois():
    """Generates a bar chart showing the volume of sales for the last 6 months."""

    conn = db.open_connection()
    cursor = conn.cursor()
    query = """
        SELECT strftime('%Y-%m', datetime(saleDate, 'unixepoch')) AS mois, COUNT(*) AS volume
        FROM userMovie
        WHERE datetime(saleDate, 'unixepoch') >= date('now', '-6 months') AND sold = 1
        GROUP BY mois
        ORDER BY mois ASC;
    """
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()

    if not data:
        logger.warning('Aucune vente enregistrée dans les 6 derniers mois.')
        return

    mois = [row[0] for row in data]
    volumes = [row[1] for row in data]

    plt.switch_backend('TkAgg')
    plt.figure(figsize=(10, 5))
    plt.bar(mois, volumes, color='skyblue')
    plt.title('Volume des ventes des 6 derniers mois')
    plt.xlabel('Mois')
    plt.ylabel('Nombre de ventes')
    plt.tight_layout()
    plt.show()


# Top 3 des utilisateurs ayant consommé le plus
def top_3_utilisateurs():
    """Retrieves the top 3 users with the highest number of purchases and displays the data in a pie chart."""

    conn = db.open_connection()
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
        logger.warning('Aucune vente enregistrée.')
        return

    utilisateurs = [row[0] for row in data]
    volumes = [row[1] for row in data]

    plt.switch_backend('TkAgg')
    plt.figure(figsize=(7, 7))
    plt.pie(volumes, labels=utilisateurs, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightcoral', 'lightskyblue'])
    plt.title('Top 3 des utilisateurs ayant consommé le plus')
    plt.tight_layout()
    plt.show()


# Top 5 des films les plus vendus
def top_5_films():
    """Retrieves the top 5 best-selling movies and displays the data in a bar chart."""

    conn = db.open_connection()
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
        logger.warning('Aucun film vendu.')
        return

    films = [row[0] for row in data]
    ventes = [row[1] for row in data]

    plt.switch_backend('TkAgg')
    plt.figure(figsize=(10, 5))
    plt.bar(films, ventes, color='lightgreen')
    plt.title('Top 5 des films les plus vendus')
    plt.xlabel('Films')
    plt.ylabel('Nombre de ventes')
    plt.tight_layout()
    plt.show()
