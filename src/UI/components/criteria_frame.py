from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.UI.app import App


class CriteriaFrame(ttk.LabelFrame):
    """
    A class representing the criteria frame for the Movie Recommendation System.

    Attributes:
    -----------
    app : App
        An instance of the main application.

    Methods:
    --------
    __init__(parent: ttk.Frame, app: App):
        Initializes the criteria frame with the given parent and app instance.
    create_widgets():
        Creates and arranges the widgets in the criteria frame.
    disable():
        Disables the filter button and combo box.
    _update_filter_process():
        Handles the filter update process by invoking the app's open_filter_frame method.
    """

    def __init__(self, parent: ttk.Frame, app: App):
        super().__init__(
            parent,
            borderwidth=2,
            relief=tk.SOLID,
            text='Critères',
        )
        self.grid(
            row=0,
            column=1,
            padx=5,
        )
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        """Create and arrange the widgets in the criteria frame."""

        self.combo = ttk.Combobox(
            self,
            values=[
                'Date',
                'Genre',
                'Age'
            ],
            state='disable'
        )
        self.combo.grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )
        self.combo.current(1)

        self.button_filter = ttk.Button(
            self,
            text='Filtres',
            command=self._update_filter_process
        )
        self.button_filter.grid(
            row=0,
            column=1,
            pady=5,
            padx=5
        )

    def disable(self):
        """Disables the filter button and combo box."""

        self.button_filter['state'] = 'disable'
        self.combo['state'] = 'disable'

    def _update_filter_process(self):
        """Handles the filter update process."""

        self.app.open_filter_frame()
