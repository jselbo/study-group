#!/usr/bin/env python3

import subprocess
import sys
from typing import List, Tuple

if len(sys.argv) < 2:
    print("Usage: validate.py <program-executable>", file=sys.stderr)
    sys.exit(1)

program_exec = sys.argv[1]


def check(program_args: List[str], expected_output: str):
    output = subprocess.check_output([program_exec] + program_args).strip().decode("utf-8")
    if output != expected_output:
        print(f"Invalid output for input `{' '.join(program_args)}`:", file=sys.stderr)
        print(f"  EXPECTED: {expected_output}", file=sys.stderr)
        print(f"  ACTUAL:   {output}", file=sys.stderr)
        return False
    return True


def check_all(args_to_output: List[Tuple[List[str], str]]):
    all_pass = True
    for args, output in args_to_output:
        case_pass = check(args, output)
        all_pass = all_pass and case_pass
    if not all_pass:
        print("Some test cases failed!", file=sys.stderr)
        sys.exit(2)


# TODO add support for future problems
check_all([
    (["123", "456"], "579"),
    (["89752897", "103420093"], "193172990"),
])
