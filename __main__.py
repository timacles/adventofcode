import utils
import argparse


def main():
    ''' the moduler AOC day solver. '''

    args = parse_args()

    if args.init:
        utils.initialize_day_module(args.day)
        return

    if args.test:
        print(f"  running tests for day {args.day}")
        return

    day_module = utils.import_module(args.day)
    input = utils.load_input_file(day_module.DAY_PATH)

    if args.part == '1':
        result = day_module.solve_part_one(input)
    elif args.part == '2':
        result = day_module.solve_part_two(input)

    print(f"  Day {args.day}, Part {args.part}")
    print(f"    === {result} ===")


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
    

if __name__ == "__main__":
    main()
