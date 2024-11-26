from pathlib import Path
import json

settings_file = Path(__file__).resolve().parent.joinpath('settings.json')


class Settings:

    def __init__(self):
        settings: dict = self.read_settings()
        self.extensions: list[ExtensionSettings] = [
            ExtensionSettings(extension)
            for extension in settings.get('extensions', {})
        ]
        self.lib_dir: str = settings.get('lib_dir', '')
        self.dirs_to_delete: list = settings.get('dirs_to_delete', [])

    def read_settings(self) -> dict:
        with open(settings_file, 'r') as file:
            return json.load(file)


class ExtensionSettings:

    def __init__(self, extension: dict):
        self.extension_name: str = extension.get('extension_name', '')
        self.sources_name: str = extension.get('sources_name', '')
