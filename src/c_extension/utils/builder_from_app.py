import os
from pathlib import Path

from src.c_extension.utils.settings import Settings
from src.utils.logging import get_logger

logger = get_logger(__name__)
settings = Settings()


def build() -> None:
    """Compiles and builds shared library files for specified extensions on both Linux and Windows platforms."""

    logger.info('Building -> Starting')

    work_dir = Path(__file__).parent.parent
    os.chdir(work_dir)

    build_dir = work_dir / settings.build_dir
    build_dir.mkdir(parents=True, exist_ok=True)

    output_dir = work_dir / settings.lib_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    for extension in settings.extensions:
        source_files = [
            f'{extension.extension_name}/{extension.sources_name}.c',
            'sqlite3/sqlite3.c',
        ]

        o_files = [
            f'{settings.build_dir}/{extension.sources_name}.o',
            f'{settings.build_dir}/sqlite3.o',
        ]

        if os.name == 'nt':  # Build for Windows
            logger.info(f'Building {extension.extension_name}.dll -> Running...')
            win_output_file = output_dir / f'{extension.extension_name}.dll'

            for i, source_file in enumerate(source_files):
                logger.info(f'Building {o_files[i]} -> Running...')
                os.system(f'gcc -c -fPIC {source_file} -o {o_files[i]} -I/usr/include')
                logger.info(f'Building {o_files[i]} -> ok')

            win_compile_command = f"gcc -shared -o {win_output_file} {' '.join(o_files)}"
            os.system(win_compile_command)
            logger.info(f'Building {extension.extension_name}.dll -> OK')

        else:  # Build for Linux
            logger.info(f'Building {extension.extension_name}.so -> Running...')
            linux_output_file = output_dir / f'{extension.extension_name}.so'

            for i, source_file in enumerate(source_files):
                logger.info(f'Building {o_files[i]} -> Running...')
                os.system(f'gcc -c -fPIC {source_file} -o {o_files[i]} -I/usr/include')
                logger.info(f'Building {o_files[i]} -> ok')

            linux_compile_command = f"gcc -shared -o {linux_output_file} {' '.join(o_files)} -L/usr/lib -lsqlite3"
            os.system(linux_compile_command)
            logger.info(f'Building {extension.extension_name}.so -> OK')

    logger.info('Building -> Completed')
