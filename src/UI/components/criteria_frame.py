from __future__ import annotations
from typing import TYPE_CHECKING
import tkinter as tk
from tkinter import ttk

if TYPE_CHECKING:
    from src.UI.app import App


class CriteriaFrame(ttk.LabelFrame):
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
        self.button_filter['state'] = 'disable'
        self.combo['state'] = 'disable'

    def _update_filter_process(self):
        self.app.open_filter_frame()
