import os
from src.c_extension.utils.settings import Settings
from src.utils.logging import get_logger
from pathlib import Path

logger = get_logger(__name__)
settings = Settings()


def build() -> None:
    """Compiles and builds shared library files for specified extensions on both Linux and Windows platforms."""

    logger.info('Building -> Starting')

    work_dir = Path(__file__).parent.parent
    os.chdir(work_dir)

    output_dir = work_dir / settings.lib_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    for extension in settings.extensions:
        source_files = [
            f'{extension.extension_name}/{extension.sources_name}.c',
            f'{extension.extension_name}/{extension.sources_name}.h',
            'sqlite3/sqlite3.c',
            'sqlite3/sqlite3.h',
        ]

        if os.name == 'nt':  # Build for Windows
            logger.info(f'Building {extension.extension_name}.dll -> Running...')
            win_output_file = output_dir / f'{extension.extension_name}.dll'
            win_compile_command = f"gcc -shared -o {win_output_file} {' '.join(source_files)} -fPIC"
            os.system(win_compile_command)
            logger.info(f'Building {extension.extension_name}.dll -> OK')

        else:  # Build for Linux
            logger.info(f'Building {extension.extension_name}.so -> Running...')
            linux_output_file = output_dir / f'{extension.extension_name}.so'
            linux_compile_command = f"gcc -shared -o {linux_output_file} {' '.join(source_files)} -I/usr/include -L/usr/lib -lsqlite3 -fPIC"
            os.system(linux_compile_command)
            logger.info(f'Building {extension.extension_name}.so -> OK')

    logger.info('Building -> Completed')
