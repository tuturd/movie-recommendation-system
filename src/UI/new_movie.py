import tkinter as tk
from tkinter import ttk
from src.utils.logging import get_logger


logger = get_logger(__name__)


class NewMovie(tk.Toplevel):
    """
    A class used to create a new movie entry window in the Movie Recommendation System.

    Attributes
    ----------
    on_destroy : function
        A callback function to be called when the window is closed.

    Methods
    -------
    __init__(self, parent, on_destroy)
        Initializes the NewMovie window with the given parent and on_destroy callback.

    create_widgets(self)
        Creates and arranges the widgets in the NewMovie window.

    on_submit(self, e=None)
        Handles the event when the user submits the new movie entry.

    close(self)
        Closes the NewMovie window and calls the on_destroy callback.
    """

    def __init__(self, parent, on_destroy):
        super().__init__(parent)
        self.on_destroy = on_destroy
        self.title('Nouveau Film - Movie Recommendation System')
        self.protocol('WM_DELETE_WINDOW', self.close)
        self.create_widgets()

    def create_widgets(self):
        """Create and arrange the widgets in the NewMovie window."""

        self.label = ttk.Label(
            self,
            text="Ajout d'un film"
        )
        self.label.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20
        )

        self.label = ttk.Label(
            self,
            text='Film :'
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
        """Handles the event when the user submits the new movie entry."""

        user_input = self.entry.get()
        logger.debug(f'film input: {user_input}')
        self.close()

    def close(self):
        """Close the NewMovie window and call the on_destroy callback."""

        self.destroy()
        self.on_destroy()
