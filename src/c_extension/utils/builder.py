import os
from utils.settings import Settings
from pathlib import Path


settings = Settings()


def build() -> None:
    """Compiles and builds shared library files for specified extensions on both Linux and Windows platforms."""

    output_dir = Path(__file__).parent.parent / settings.lib_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    for extension in settings.extensions:
        source_files = [
            f'{extension.extension_name}/{extension.sources_name}.c',
            f'{extension.extension_name}/{extension.sources_name}.h',
            'sqlite3/sqlite3.c',
            'sqlite3/sqlite3.h',
        ]

        if os.name == 'nt':
            win_output_file = output_dir / f'{extension.extension_name}.dll'
            win_compile_command = f"gcc -shared -o {win_output_file} {' '.join(source_files)} -fPIC"
            os.system(win_compile_command)

        else:
            linux_output_file = output_dir / f'{extension.extension_name}.so'
            linux_compile_command = f"gcc -shared -o {linux_output_file} {' '.join(source_files)} -I/usr/include -L/usr/lib -lsqlite3 -fPIC"
            os.system(linux_compile_command)


if __name__ == '__main__':
    build()
    print("Build completed. Please run the script 'extension.py' instead.")  # noqa: T201
