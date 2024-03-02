import subprocess
import sys
from typing import List, Tuple

def check(program_exec: str, program_args: List[str], expected_output: str):
    output = subprocess.check_output([program_exec] + program_args).strip().decode("utf-8")
    if output != expected_output:
        print(f"Invalid output for input `{' '.join(program_args)}`:", file=sys.stderr)
        print(f"  EXPECTED: {expected_output}", file=sys.stderr)
        print(f"  ACTUAL:   {output}", file=sys.stderr)
        return False
    return True


def check_all(program_exec: str, args_to_output: List[Tuple[List[str], str]]):
    all_pass = True
    for args, output in args_to_output:
        case_pass = check(program_exec, args, output)
        all_pass = all_pass and case_pass
    if not all_pass:
        print("Some test cases failed!", file=sys.stderr)
        sys.exit(2)
    else:
        print("Passed all test cases!")


def p1_runner(args):
  test_cases = [
    (["123", "456"], "579"),
    (["89752897", "103420093"], "193172990"),
    (["0", "0"], "0"),
    (["98204389028349082340899", "723487239847892347987234"], "821691628876241430328133"),
    (["340282366920938463463374607431768211455", "340282366920938463463374607431768211455"], "680564733841876926926749214863536422910"),
  ]
  check_all(args.program_exec, test_cases)
