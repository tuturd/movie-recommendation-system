import sys
import database.seed.seed_by_cli as seed_by_cli
import database.seed.example_data_by_cli as example_data_by_cli

if __name__ == '__main__':
    arg = sys.argv[1] if len(sys.argv) > 1 else None

    match arg:
        case 'seed':
            seed_by_cli.seed_database()
        case 'example_data':
            example_data_by_cli.import_example_data()
        case _:
            print('Please provide an argument: seed')  # noqa: T201
            sys.exit(1)
