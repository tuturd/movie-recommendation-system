from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.UI.app import App


class FilterFrame(ttk.LabelFrame):
    """
    A class representing the filter frame for the Movie Recommendation System.

    Attributes:
    -----------
    app : App
        The main application instance.

    Methods:
    --------
    __init__(parent: ttk.Frame, app: App):
        Initializes the filter frame with the given parent and app instance.
    create_widgets():
        Creates and arranges the widgets in the filter frame.
    on_submit():
        Handles the submission of the filters and performs the necessary actions.
    """

    def __init__(self, parent: ttk.Frame, app: App):
        super().__init__(
            parent,
            borderwidth=2,
            relief=tk.SOLID,
            text='Filtres',
        )
        self.grid(
            row=0,
            column=2,
            padx=5
        )
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        """Create and arrange the widgets in the filter frame."""

        self.button_filter = ttk.Button(
            self,
            text='Filtres',
            command=lambda: None,
        )
        self.button_filter.grid(
            row=0,
            column=0,
            pady=5,
            padx=5
        )

        self.button_filter = ttk.Button(
            self,
            text='Filtres',
            command=lambda: None,
        )
        self.button_filter.grid(
            row=0,
            column=1,
            pady=5,
            padx=5
        )

        self.button_filter = ttk.Button(
            self,
            text='Filtres',
            command=lambda: None,
        )
        self.button_filter.grid(
            row=0,
            column=2,
            pady=5,
            padx=5
        )

        self.button_filter = ttk.Button(
            self,
            text='Filtres',
            command=lambda: None,
        )
        self.button_filter.grid(
            row=0,
            column=3,
            pady=5,
            padx=5
        )

        self.button_submit = ttk.Button(
            self,
            text='Valider',
            command=self.on_submit,
        )
        self.button_submit.grid(
            row=0,
            column=4,
            pady=5,
            padx=5
        )

    def on_submit(self):
        """Handle the submission of the filters and perform the necessary actions."""

        self.app.close_filter_frame()
        self.app.create_widgets()
