from .settings import Settings
from pathlib import Path

settings = Settings()

# Paths to the directories to be deleted
current_dir = Path(__file__).resolve().parent.parent


def delete_directory(directory):
    """
    Recursively delete a directory and all its contents.

    Parameters:
    -----------
    directory : pathlib.Path
        The path to the directory to be deleted.
    """

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


def delete_file(directory):
    """
    Delete a file from the specified directory.

    Parameters:
    -----------
    directory : str
        The path to the file to be deleted.
    """

    try:
        Path.unlink(directory)
        print(f'Deleted file: {directory}')  # noqa: T201
    except FileNotFoundError:
        print(f'File does not exist: {directory}')  # noqa: T201


def reset() -> None:
    """
    Reset the environment by deleting specified directories and compiled files.
    This function performs the following actions:
    1. Deletes directories listed in `settings.dirs_to_delete`.
    2. Deletes compiled files with extensions listed in `settings.extensions`.
    """

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
