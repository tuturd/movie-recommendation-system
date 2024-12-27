import tkinter as tk
from src.database.utils import admin as AdminUtils


class AdminInterface(tk.Toplevel):

    def __init__(self, parent, on_destroy):
        super().__init__(parent)
        self.on_destroy = on_destroy
        self.title('Tableau de bord - Movie Recommendation System')
        self.protocol('WM_DELETE_WINDOW', self.close)
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text='Exporter les ventes en CSV', command=AdminUtils.exporter_ventes).pack(pady=10)

        # Boutons pour afficher les graphiques
        self.btn_volume = tk.Button(self, text='Volume des ventes (6 derniers mois)', command=AdminUtils.volume_6_mois)
        self.btn_volume.pack(pady=10)

        self.btn_top_users = tk.Button(self, text='Top 3 des utilisateurs', command=AdminUtils.top_3_utilisateurs)
        self.btn_top_users.pack(pady=10)

        self.btn_top_movies = tk.Button(self, text='Top 5 des films les plus vendus', command=AdminUtils.top_5_films)
        self.btn_top_movies.pack(pady=10)

    def close(self):
        self.destroy()
        self.on_destroy()


# def main():
#     root = tk.Tk()
#     root.title('Tableau de bord - Gestion des ventes')

#     # Boutons pour gérer les ventes
#     tk.Button(root, text='Ajouter une vente', command=lambda: AdminUtils.ajouter_vente(1, 1)).pack(pady=10)
#     tk.Button(root, text='Exporter les ventes en CSV', command=AdminUtils.exporter_ventes).pack(pady=10)

#     # Boutons pour afficher les graphiques
#     tk.Button(root, text='Volume des ventes (6 derniers mois)', command=AdminUtils.volume_6_mois).pack(pady=10)
#     tk.Button(root, text='Top 3 des utilisateurs', command=AdminUtils.top_3_utilisateurs).pack(pady=10)
#     tk.Button(root, text='Top 5 des films les plus vendus', command=AdminUtils.top_5_films).pack(pady=10)

#     root.mainloop()


# if __name__ == '__main__':
#     main()
