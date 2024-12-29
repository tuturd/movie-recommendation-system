from src.UI.app import App

try:
    App().mainloop()  # Lancement de l'application
except KeyboardInterrupt:
    exit()  # Fermeture de l'application
