from tkinter import messagebox
from src.database.seed.seed_by_app import seed_database
from src.database.seed.example_data_by_app import import_example_data


def starting_sequence():
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
