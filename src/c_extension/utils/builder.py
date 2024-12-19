import os
from utils.settings import Settings
from pathlib import Path


settings = Settings()


def build() -> None:
    output_dir = Path(__file__).parent.parent / settings.lib_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    for extension in settings.extensions:
        source_files = [
            f'{extension.extension_name}/{extension.sources_name}.c',
            f'{extension.extension_name}/{extension.sources_name}.h',
        ]
        output_file = output_dir / f'{extension.extension_name}.so'
        compile_command = f"gcc -shared -o {output_file} {' '.join(source_files)} -I/usr/include -L/usr/lib -lsqlite3 -fPIC"
        os.system(compile_command)


if __name__ == '__main__':
    build()
    print("Build completed. Please run the script 'extension.py' instead.")  # noqa: T201
