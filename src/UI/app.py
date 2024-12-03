import tkinter as tk
from tkinter import ttk
from src.UI.auth import Auth
from src.UI.components.actions_frame import ActionsFrame
from src.UI.components.criteria_frame import CriteriaFrame
from src.UI.components.filter_frame import FilterFrame
from src.UI.components.category_container_frame import CategoryContainerFrame
from src.UI.components.category_frame import CategoryFrame
from src.utils.logging import get_logger


logger = get_logger(__name__)


class App(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__()
        self.title('Movie Recommendation System')
        self.auth: Auth = self.auth_process()
        self.filter_frame_open: bool = kwargs.get('filter_frame_open', False)
        self.label_title: ttk.Label = None
        self.button_logout: ttk.Button = None
        self.frame_actions: ActionsFrame = None
        self.frame_criteria: CriteriaFrame = None
        self.frame_filter: FilterFrame = None
        self.categories: list[CategoryFrame] = []

    def create_widgets(self):
        self.label_title = ttk.Label(
            self,
            text=f'Bienvenue sur le système de recommendation, {self.auth.username} !',
            anchor=tk.CENTER
        )
        self.label_title.grid(
            row=0,
            column=0,
            columnspan=2
        )

        self.button_logout = ttk.Button(
            self,
            text='Deconnexion',
            command=self.auth_process
        )
        self.button_logout.grid(
            row=0,
            column=1,
            pady=5,
            padx=5,
            sticky='e'
        )

        self.frame_actions = ActionsFrame(self)

        self.frame_criteria = CriteriaFrame(self)

        if self.filter_frame_open:
            self.frame_filter = FilterFrame(self)
        else:
            if self.frame_filter and self.frame_filter.winfo_exists():
                self.frame_filter.destroy()

        self.frame_category = CategoryContainerFrame(self)

    def disable(self):
        self.button_logout['state'] = 'disable'
        self.frame_actions.disable()
        self.frame_criteria.disable()

    def auth_process(self) -> Auth:
        self.withdraw()
        return Auth(self.on_auth_destroy)

    def on_auth_destroy(self):
        self.deiconify()
        self.create_widgets()


if __name__ == '__main__':
    app = App()
    app.mainloop()
