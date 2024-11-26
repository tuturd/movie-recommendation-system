import sys
from utils.builder import build
from utils.reset import reset

if __name__ == '__main__':
    arg = sys.argv[1] if len(sys.argv) > 1 else None

    match arg:
        case 'build':
            build()
        case 'reset':
            reset()
        case _:
            print('Please provide an argument: build or reset')  # noqa: T201
            sys.exit(1)
