from tkinter import messagebox

from src.database.seed.example_data_by_app import import_example_data
from src.database.seed.seed_by_app import seed_database


def starting_sequence():
    """
    Handles the initial startup sequence for the application.

    This function prompts the user with a series of message boxes to determine
    if they have previously used the application on the current computer and
    if the database has been initialized. Based on the user's responses, it
    may initialize the database and import example data. It also provides
    information on how to connect to a user or the administration interface.

    Exits the application if the user cancels any of the prompts.
    """
    res = messagebox.askyesnocancel('Démarrage', 'Avez-vous déjà utilisé cette application sur cet ordinateur ?')
    if res is True:
        return
    elif res is None:
        exit()

    res = messagebox.askyesnocancel('Base de donnée', 'Avez-vous déjà initialisé la base de donnée ?')
    if res is False:
        seed_database()
        import_example_data()
    elif res is None:
        exit()

    messagebox.showinfo('Information', 'Pour vous connecter à un utilisateur, entrez son pseudo. Par exemple : \"johndoe\"')
    messagebox.showinfo('Information', 'Pour vous connecter à l\'interface d\'administration, entrez \"admin\"')
