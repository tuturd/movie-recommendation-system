import sys
import seed.seed as seed
import seed.example_data as example_data

if __name__ == '__main__':
    arg = sys.argv[1] if len(sys.argv) > 1 else None

    match arg:
        case 'seed':
            seed.seed_database()
        case 'example_data':
            example_data.import_example_data()
        case _:
            print('Please provide an argument: seed')  # noqa: T201
            sys.exit(1)
