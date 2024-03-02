#!/usr/bin/env python3
import argparse
import sys
import p1
import p2

# python3 validator/validate.py p1 --program_exec don/p1/runner.sh
# python3 validator/validate.py p2 --program_exec don/p2/runner.sh
def main() -> int:
    parser = argparse.ArgumentParser()
    try:
        subparsers = parser.add_subparsers()

        parser_p1 = subparsers.add_parser('p1')
        parser_p1.add_argument('--program_exec', type=str, required=True)
        parser_p1.set_defaults(func=p1.p1_runner)

        parser_p2 = subparsers.add_parser('p2')
        parser_p2.add_argument('--program_exec', type=str, required=True)
        parser_p2.set_defaults(func=p2.p2_runner)

        args = parser.parse_args()
        args.func(args)
    except argparse.ArgumentTypeError as e:
        parser.print_help()
    except Exception as e:
        print("Error: ", e)
        sys.exit()

    return 0


if __name__ == '__main__':
    main()
