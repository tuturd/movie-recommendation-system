from pathlib import Path
import json

settings_file = Path(__file__).resolve().parent.joinpath('settings.json')


class Settings:
    """
    A class to manage settings for the movie recommendation system.

    Methods:
    --------
    __init__():
        Initializes the Settings object by reading settings from a file and setting up attributes.
    read_settings() -> dict:
        Reads settings from a JSON file and returns them as a dictionary.
    """

    def __init__(self):
        settings: dict = self.read_settings()
        self.extensions: list[ExtensionSettings] = [
            ExtensionSettings(extension)
            for extension in settings.get('extensions', {})
        ]
        self.lib_dir: str = settings.get('lib_dir', '')
        self.dirs_to_delete: list = settings.get('dirs_to_delete', [])

    def read_settings(self) -> dict:
        """Read settings from a JSON file and return them as a dictionary."""

        with open(settings_file, 'r') as file:
            return json.load(file)


class ExtensionSettings:
    """
    A class to handle settings for an extension.

    Parameters:
    -----------
    extension : dict
        A dictionary containing extension settings.

    Attributes:
    -----------
    extension_name : str
        The name of the extension.
    sources_name : str
        The name of the sources associated with the extension.
    """

    def __init__(self, extension: dict):
        self.extension_name: str = extension.get('extension_name', '')
        self.sources_name: str = extension.get('sources_name', '')
