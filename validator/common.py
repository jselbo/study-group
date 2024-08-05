import subprocess
import sys
from typing import List


def validate_output(program_exec: str, program_args: List[str], expected_output: str) -> bool:
    output = subprocess.check_output([program_exec] + program_args).strip().decode("utf-8")
    if output != expected_output:
        print(f"Invalid output for input `{' '.join(program_args)}`:", file=sys.stderr)
        print(f"  EXPECTED: {expected_output}", file=sys.stderr)
        print(f"  ACTUAL:   {output}", file=sys.stderr)
        return False
    return True
