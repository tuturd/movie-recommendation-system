import tkinter as tk
from tkinter import messagebox
import sys
import os

# Ajouter le chemin du dossier parent au PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../admin')))

# Importer les fonctionnalités depuis le dossier admin
import fonctionnalites


def main():
    root = tk.Tk()
    root.title("Tableau de bord - Gestion des ventes")

    # Boutons pour gérer les ventes
    tk.Button(root, text="Ajouter une vente", command=lambda: fonctionnalites.ajouter_vente(1, 1)).pack(pady=10)
    tk.Button(root, text="Exporter les ventes en CSV", command=fonctionnalites.exporter_ventes).pack(pady=10)

    # Boutons pour afficher les graphiques
    tk.Button(root, text="Volume des ventes (6 derniers mois)", command=fonctionnalites.volume_6_mois).pack(pady=10)
    tk.Button(root, text="Top 3 des utilisateurs", command=fonctionnalites.top_3_utilisateurs).pack(pady=10)
    tk.Button(root, text="Top 5 des films les plus vendus", command=fonctionnalites.top_5_films).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
