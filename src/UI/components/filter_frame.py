from __future__ import annotations
from typing import TYPE_CHECKING
import tkinter as tk
from tkinter import ttk

if TYPE_CHECKING:
    from src.UI.app import App


class FilterFrame(ttk.LabelFrame):
    def __init__(self, parent: App):
        super().__init__(
            parent,
            borderwidth=2,
            relief=tk.SOLID,
            text='Filtres',
        )
        self.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=5
        )
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
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
        self.parent.filter_frame_open = False
        self.parent.create_widgets()
