import tkinter as tk
import src.database.utils.auth as auth
from tkinter import ttk
from src.utils.logging import get_logger
from src.utils.start import starting_sequence
from src.UI.interface import AdminInterface


logger = get_logger(__name__)


class Auth(tk.Tk):
    """
    A class representing the authentication window for the Movie Recommendation System.
    Attributes:
    -----------
    on_destroy : function
        A callback function to be called when the window is destroyed.
    on_username_error : bool
        A flag indicating whether there was an error with the username.
    username : str
        The username entered by the user.
    Methods:
    --------
    __init__(on_destroy):
        Initializes the authentication window with the given on_destroy callback.
    create_widgets():
        Creates and arranges the widgets in the authentication window.
    on_submit():
        Handles the submission of the username and performs validation.
    """

    def __init__(self, on_destroy, auth_number):
        super().__init__()
        self.on_destroy = on_destroy
        self.auth_number = auth_number
        self.auth_error = ''
        self.username = ''

        self.title('Connexion - Movie Recommendation System')
        self.protocol('WM_DELETE_WINDOW', exit)

        self.label_title: ttk.Label = None
        self.label_username: ttk.Label = None
        self.label_error: ttk.Label = None
        self.label_credits: ttk.Label = None
        self.button_login: ttk.Button = None
        self.button_signin: ttk.Button = None

        if self.auth_number == 1:
            self.withdraw()
            starting_sequence()
            self.deiconify()

        self.create_widgets()

    def create_widgets(self):
        """Create and arrange the widgets in the authentication window."""

        self.label_title = ttk.Label(
            self,
            text='Portail de connexion'
        )
        self.label_title.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20
        )

        self.label_username = ttk.Label(
            self,
            text='Pseudo :'
        )
        self.label_username.grid(
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

        if self.label_error and self.label_error.winfo_exists():
            self.label_error.destroy()
        if self.auth_error:
            self.label_error = ttk.Label(
                self,
                text=self.auth_error,
                foreground='red'
            )
            self.label_error.grid(
                row=2,
                column=0,
                columnspan=2,
                pady=10
            )

        self.button_login = ttk.Button(
            self,
            text='Connexion',
            command=self.on_submit
        )
        self.button_login.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=10,
            sticky='ew'
        )

        self.button_signin = ttk.Button(
            self,
            text='Créer un compte',
            command=self.signin_process
        )
        self.button_signin.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=10,
            sticky='ew'
        )

        self.label_credits = ttk.Label(
            self,
            text='Projet Final NF06 - A24\nArthur Dodin - Eliott Tardif',
            anchor='center'
        )
        self.label_credits.grid(
            row=5,
            column=0,
            columnspan=2,
            pady=10,
            sticky='ew'
        )

    def on_submit(self, e=None):
        """Handles the event when the user submits the username."""

        user_input = self.entry.get()
        logger.debug(f'Username input: {user_input}')

        try:
            if auth.login(user_input):
                self.username = user_input
                self.close()
                return
            elif user_input == 'admin':
                self.username = user_input
                self.admin_interface = AdminInterface(self, self.on_admin_interface_destroy)
            else:
                self.auth_error = 'Utilisateur introuvable'
            self.create_widgets()

        except auth.LoginError as error:
            logger.error(error)
            self.auth_error = error.message
            self.create_widgets()

    def on_admin_interface_destroy(self):
        """Handles the event when the admin interface is destroyed."""

        pass

    def signin_process(self):
        """Handles the event when the user clicks on the 'Créer un compte' button."""

        logger.debug('Signin process not inplemented')

    def close(self):
        """Closes the authentication window and calls the on_destroy callback."""

        self.destroy()
        self.on_destroy()
