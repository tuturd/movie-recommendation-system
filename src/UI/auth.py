import tkinter as tk
import src.database.utils.auth as auth
from tkinter import ttk
from src.utils.logging import get_logger


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

    def __init__(self, on_destroy):
        super().__init__()
        self.on_destroy = on_destroy
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

        self.create_widgets()

    def create_widgets(self):
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
        user_input = self.entry.get()
        logger.debug(f'Username input: {user_input}')

        try:
            if auth.login(user_input):
                self.username = user_input
                self.close()
                return
            elif user_input == 'admin':
                self.username = user_input
                self.auth_error = 'Page indisponible'
                logger.debug('Administrator page not implemented')
            else:
                self.auth_error = 'Utilisateur introuvable'
            self.create_widgets()

        except auth.LoginError as error:
            logger.error(error)
            self.auth_error = error.message
            self.create_widgets()

    def signin_process(self):
        logger.debug('Signin process not inplemented')

    def close(self):
        self.destroy()
        self.on_destroy()
