from __future__ import annotations
from typing import TYPE_CHECKING
import tkinter as tk
from tkinter import ttk
from src.utils.logging import get_logger
from src.database.utils.user import get_user_profile

if TYPE_CHECKING:
    from src.UI.app import App


logger = get_logger(__name__)


class Profile(tk.Toplevel):

    def __init__(self, parent: App, on_destroy):
        super().__init__(parent)
        self.parent = parent
        self.on_destroy = on_destroy
        self.title('Mon Profil - Movie Recommendation System')
        self.protocol('WM_DELETE_WINDOW', self.close)
        self.profile = get_user_profile(self.parent.user.id)
        self.create_widgets()

    def create_widgets(self):
        self.label_name = ttk.Label(
            self,
            text=f'{self.parent.user.firstname} {self.parent.user.lastname}'
        )
        self.label_name.grid(
            row=0,
            column=0,
        )

        self.label_username = ttk.Label(
            self,
            text=f'Pseudonyme : {self.parent.user.username}'
        )
        self.label_username.grid(
            row=0,
            column=1,
        )

        self.label_birth_date = ttk.Label(
            self,
            text=f'Date de naissance : {self.parent.user.birth_date}'
        )
        self.label_birth_date.grid(
            row=2,
            column=0,
        )

        self.label_director = ttk.Label(
            self,
            text=f'réalisateurs préférés : 1. {self.profile.directors[0].firstname} {self.profile.directors[0].lastname} 2. {self.profile.directors[1].firstname} {self.profile.directors[1].lastname} 3. {self.profile.directors[2].firstname} {self.profile.directors[2].lastname}'
        )
        self.label_director.grid(
            row=3,
            column=0,
        )

        self.label_director = ttk.Label(
            self,
            text=f'genres préférés : 1. {self.profile.genres[0].name} 2. {self.profile.genres[1].name} 3. {self.profile.genres[2].name}'
        )
        self.label_director.grid(
            row=4,
            column=0,
        )

    def close(self):
        self.destroy()
        self.on_destroy()
