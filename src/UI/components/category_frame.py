from __future__ import annotations
from typing import TYPE_CHECKING
import tkinter as tk
from tkinter import ttk

if TYPE_CHECKING:
    from src.UI.components.category_container_frame import CategoryContainerFrame


class CategoryFrame(ttk.Frame):
    def __init__(self, parent: CategoryContainerFrame, **kwargs):
        super().__init__(
            parent
        )
        self.pack(
            padx=kwargs.get('padx', 5),
            pady=kwargs.get('pady', 5),
        )
        self.parent = parent
        self.kwargs = kwargs
        self.create_widgets()

    def create_widgets(self):
        self.label_title = ttk.Label(
            self,
            text=self.kwargs.get('title', 'Catégorie sans titre'),
            anchor=tk.CENTER
        )
        self.label_title.grid(
            row=0,
            column=0,
            columnspan=2
        )
