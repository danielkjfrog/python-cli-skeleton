import argparse
from . import _program

def main():
    parser = argparse.ArgumentParser(prog = _program)
    parser.add_argument("--int_value",
                        help="display a square of a given number",
                        type=int)

    parser.add_argument("--float_value",
                        help="display a square of a given number",
                        type=int)

    parser.add_argument("-f",
                        "--flag",
                        help="Specify a flag",
                        action="store_true")
    parser.add_argument("--rating",
                        help="An option with a limited range of values",
                        choices=[1, 2, 3],
                        type=int)

    # Allow --day and --night options, but not together.
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--day",
                       help = "mutually exclusive option",
                       action = "store_true")
    group.add_argument("--night",
                       help = "mutually exclusive option",
                       action = "store_true")

    args = parser.parse_args()

    print("Arguments")
    print("value: " + str(args.int_value))
    print("value: " + str(args.float_value))
    print("flag: " + str(args.flag))
    print("rating: " + str(args.rating))

if __name__ == '__main__':
    main()
