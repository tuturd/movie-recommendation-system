from .settings import Settings
from pathlib import Path

settings = Settings()

# Paths to the directories to be deleted
current_dir = Path(__file__).resolve().parent.parent


# Function to delete a directory if it exists
def delete_directory(directory):
    try:
        for item in directory.iterdir():
            if item.is_dir():
                delete_directory(item)
            else:
                item.unlink()
        directory.rmdir()
        print(f'Deleted directory: {directory}')  # noqa: T201
    except FileNotFoundError:
        print(f'Directory does not exist: {directory}')  # noqa: T201


# Function to delete a file if it exists
def delete_file(directory):
    try:
        Path.unlink(directory)
        print(f'Deleted file: {directory}')  # noqa: T201
    except FileNotFoundError:
        print(f'File does not exist: {directory}')  # noqa: T201


def reset() -> None:
    # Delete the directories
    for directory in settings.dirs_to_delete:
        delete_directory(current_dir.joinpath(directory))

    # Delete the compiled files
    for extension in settings.extensions:
        delete_file(current_dir.joinpath(
            extension.extension_name,
            f'{extension.extension_name}.c'
        ))


if __name__ == '__main__':
    print("Please run the script 'extension.py' instead.")  # noqa: T201
