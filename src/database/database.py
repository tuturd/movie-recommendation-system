import sys

import seed.example_data_by_cli as example_data_by_cli
import seed.seed_by_cli as seed_by_cli

if __name__ == '__main__':
    # Get the first argument passed to the script, if any set to None
    arg = sys.argv[1] if len(sys.argv) > 1 else None

    match arg:
        case 'seed':
            seed_by_cli.seed_database()  # Start the database seeding
        case 'example_data':
            example_data_by_cli.import_example_data()  # Import the example data sets
        case _:
            print('Please provide an argument: seed')  # noqa: T201
            sys.exit(1)
