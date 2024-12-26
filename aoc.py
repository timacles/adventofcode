import utils
import argparse
import unittest
from shutil import get_terminal_size


def main():
    ''' the moduler AOC day solver. '''

    args = parse_args()

    if args.init:
        utils.initialize_day_module(args.day)
        return

    day_module = utils.import_module(args.day)

    if args.test:
        run_tests(args.day)
        return

    input = utils.load_input_file(day_module.DAY_PATH)

    if args.part == '1':
        result = day_module.solve_part_one(input)
    elif args.part == '2':
        result = day_module.solve_part_two(input)

    print(f"\n {YELLOW}", "-" * (get_terminal_size().columns - 3))
    print(f"  {GREEN}Day {args.day}, Part {args.part}, RESULT => {RED}{result}{RESET}\n")


GREEN='\033[32m'
RED='\033[31m'
YELLOW='\033[33m'
RESET='\033[0m'


def parse_args():
    parser = argparse.ArgumentParser(description="Script with boolean and integer arguments.")
    parser.add_argument(
        '--init', 
        action='store_true', 
        help="Initialize the module."
    )
    parser.add_argument(
        '--test', 
        action='store_true', 
        help="Run unit tests."
    )
    parser.add_argument(
        '--day', 
        type=str, 
        required=True, 
        help="Specify the day (required integer argument)."
    )
    parser.add_argument(
        '--part', 
        type=str, 
        default="1",
        choices=["1","2"],
        help="Specify the part (required integer argument)."
    )
    return parser.parse_args()
    

def run_tests(day):
    """Discover and run tests."""
    # Load the tests directly from the `day1` module
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(__import__('day' + day))

    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2, failfast=True)
    result = runner.run(suite)

    # Exit with the appropriate status code
    exit(0 if result.wasSuccessful() else 1)

if __name__ == "__main__":
    main()
