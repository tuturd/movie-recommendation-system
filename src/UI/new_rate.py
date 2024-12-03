import tkinter as tk
from tkinter import ttk
from src.utils.logging import get_logger


logger = get_logger(__name__)


class NewRate(tk.Toplevel):

    def __init__(self, parent, on_destroy):
        super().__init__(parent)
        self.on_destroy = on_destroy
        self.title('Nouvelle note - Movie Recommendation System')
        self.protocol('WM_DELETE_WINDOW', self.close)
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(
            self,
            text="Ajout d'une note"
        )
        self.label.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20
        )

        self.label = ttk.Label(
            self,
            text='Note :'
        )
        self.label.grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        self.entry = ttk.Entry(
            self,
        )
        self.entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )
        self.entry.focus_set()
        self.entry.bind('<Return>', self.on_submit)

        self.button = ttk.Button(
            self,
            text='Ajouter',
            command=self.on_submit
        )
        self.button.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=10,
            sticky='ew'
        )

    def on_submit(self, e=None):
        user_input = self.entry.get()
        logger.debug(f'rate input: {user_input}')
        self.close()

    def close(self):
        self.destroy()
        self.on_destroy()
