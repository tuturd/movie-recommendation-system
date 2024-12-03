import tkinter as tk
from tkinter import ttk
from src.utils.logging import get_logger


logger = get_logger(__name__)


class NewUser(tk.Toplevel):

    def __init__(self, parent, on_destroy):
        super().__init__(parent)
        self.on_destroy = on_destroy
        self.title('Nouvel utilisateur - Movie Recommendation System')
        self.protocol('WM_DELETE_WINDOW', self.close)
        self.create_widgets()

    def create_widgets(self):
        self.label_title = ttk.Label(
            self,
            text='Nouvel utilisateur'
        )
        self.label_title.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20
        )

    def close(self):
        self.destroy()
        self.on_destroy()
