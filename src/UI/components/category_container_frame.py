from __future__ import annotations
from typing import TYPE_CHECKING
from tkinter import ttk
from src.UI.components.category_frame import CategoryFrame

if TYPE_CHECKING:
    from src.UI.app import App


class CategoryContainerFrame(ttk.Frame):
    def __init__(self, parent: App, **kwargs):
        super().__init__(
            parent
        )
        self.grid(
            row=3,
            column=0,
            columnspan=2
        )
        self.parent = parent
        self.kwargs = kwargs
        self.categories: list[CategoryFrame] = []
        self.create_widgets()

    def create_widgets(self):
        self.categories = [
            CategoryFrame(
                self,
                title=cat
            )
            for id, cat in enumerate(['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5', 'Category 6'])
        ]
