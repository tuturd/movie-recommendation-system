import tkinter as tk
from tkinter import ttk
from src.utils.logging import get_logger
from src.database.utils import director as DirectorUtils


logger = get_logger(__name__)


class NewDirector(tk.Toplevel):
    """
    A class to create a new director entry window in the Movie Recommendation System.

    Attributes:
    -----------
    on_destroy : function
        A callback function to be called when the window is closed.

    Methods:
    --------
    __init__(self, parent, on_destroy):
        Initializes the NewDirector window with the given parent and on_destroy callback.

    create_widgets(self):
        Creates and arranges the widgets in the NewDirector window.

    on_submit(self, e=None):
        Handles the submission of the new director form. Validates the input and inserts the new director into the database.

    _is_well_completed(self, value: str) -> bool:
        Checks if the given value is well-formed (contains only alphabetic characters or hyphens and is not empty).

    close(self):
        Closes the NewDirector window and calls the on_destroy callback.
    """

    def __init__(self, parent, on_destroy):
        super().__init__(parent)
        self.on_destroy = on_destroy
        self.title('Nouveau Producteur - Movie Recommendation System')
        self.protocol('WM_DELETE_WINDOW', self.close)
        self.create_widgets()

    def create_widgets(self):
        """Create and arrange the widgets in the NewDirector window."""

        self.label = ttk.Label(
            self,
            text="Ajout d'un producteur"
        )
        self.label.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20
        )

        self.firstname_label = ttk.Label(
            self,
            text='Prénom :'
        )
        self.firstname_label.grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        self.firstname_entry = ttk.Entry(
            self,
        )
        self.firstname_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )
        self.firstname_entry.focus_set()

        self.lastname_label = ttk.Label(
            self,
            text='Nom :'
        )
        self.lastname_label.grid(
            row=2,
            column=0,
            padx=10,
            pady=10
        )

        self.lastname_entry = ttk.Entry(
            self,
        )
        self.lastname_entry.grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )
        self.lastname_entry.bind('<Return>', self.on_submit)

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
        """Handles the submission of the new director form."""

        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        if self._is_well_completed(firstname) and self._is_well_completed(lastname):
            DirectorUtils.insert(firstname, lastname)
            self.close()

    def _is_well_completed(self, value: str) -> bool:
        """Check if the given value is well-formed (contains only alphabetic characters or hyphens and is not empty)."""

        return all(c.isalpha() or c == '-' for c in value) and value != ''

    def close(self):
        """Close the NewDirector window and call the on_destroy callback."""

        self.destroy()
        self.on_destroy()
