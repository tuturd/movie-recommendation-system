from __future__ import annotations
from typing import TYPE_CHECKING
import tkinter as tk
from tkinter import ttk

if TYPE_CHECKING:
    from src.UI.app import App


class CriteriaFrame(ttk.LabelFrame):
    def __init__(self, parent: App):
        super().__init__(
            parent,
            borderwidth=2,
            relief=tk.SOLID,
            text='Critères',
        )
        self.grid(
            row=1,
            column=1,
            padx=5
        )
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        self.button_filter = ttk.Button(
            self,
            text='Filtres',
            command=self.update_filter_process
        )
        self.button_filter.grid(
            row=0,
            column=0,
            pady=5,
            padx=5
        )

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
            column=1,
            padx=5,
            pady=5
        )
        self.combo.current(1)

    def disable(self):
        self.button_filter['state'] = 'disable'
        self.combo['state'] = 'disable'

    def update_filter_process(self):
        self.parent.filter_frame_open = True
        self.parent.create_widgets()
        self.parent.disable()
