import tkinter as tk
from tkinter import ttk
from src.utils.logging import get_logger


logger = get_logger(__name__)


class NewUser(tk.Toplevel):
    """
    A class to create a new user window in the Movie Recommendation System UI.

    Attributes:
    -----------
    on_destroy : function
        A callback function to be called when the window is closed.

    Methods:
    --------
    __init__(parent, on_destroy):
        Initializes the new user window with the given parent and on_destroy callback.
    create_widgets():
        Creates and arranges the widgets in the new user window.
    close():
        Closes the window and calls the on_destroy callback.
    """

    def __init__(self, parent, on_destroy):
        super().__init__(parent)
        self.on_destroy = on_destroy
        self.title('Nouvel utilisateur - Movie Recommendation System')
        self.protocol('WM_DELETE_WINDOW', self.close)
        self.create_widgets()

    def create_widgets(self):
        """Create and arrange the widgets in the new user window."""

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
        """Close the window and call the on_destroy callback."""

        self.destroy()
        self.on_destroy()
