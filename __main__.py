import utils
import argparse


def main():
    args = parse_args()


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
        type=int, 
        required=True, 
        help="Specify the day (required integer argument)."
    )
    parser.add_argument(
        '--part', 
        type=int, 
        required=True, 
        help="Specify the part (required integer argument)."
    )
    return parser.parse_args()
    

if __name__ == "__main__":
    main()
