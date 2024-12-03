from setuptools import setup, Extension
from Cython.Build import cythonize
from utils.settings import Settings

settings = Settings()

extensions = [
    Extension(
        extension.extension_name,
        sources=[
            f'{extension.extension_name}/{extension.extension_name}.pyx',
            f'{extension.extension_name}/{extension.sources_name}.c',
        ],
        libraries=['sqlite3'],  # Ajoutez cette ligne pour lier la bibliothèque SQLite
        include_dirs=['/usr/include'],  # Chemin vers les fichiers d'en-tête SQLite
        library_dirs=['/usr/lib'],  # Chemin vers les bibliothèques SQLite
        language='c'
    )
    for extension in settings.extensions
]


def build() -> None:
    setup(
        name='double',
        ext_modules=cythonize(extensions, show_all_warnings=True),
        script_args=['build_ext', '--inplace', '--build-lib', settings.lib_dir]  # Indique où construire l'extension compilée
    )


if __name__ == '__main__':
    print("Please run the script 'extension.py' instead.")  # noqa: T201
