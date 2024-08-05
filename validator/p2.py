import tempfile
import subprocess
import sys
from typing import List, Tuple
from common import validate_output

def check(program_exec: str, input: str, expected_output: str) -> bool:
    return validate_output(program_exec, [input], expected_output)

def make_file(input: List[str]) -> str:
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        for i in range(len(input) - 1):
            temp_file.write(input[i] + '\n')

        if input:
            temp_file.write(input[-1])

    temp_file_path = temp_file.name

    return temp_file_path

def check_all(program_exec: str, args_to_output: List[Tuple[List[str], str]]):
    all_pass = True
    for args, output in args_to_output:
        temp_file_path = make_file(args)
        case_pass = check(program_exec, temp_file_path, output)
        all_pass = all_pass and case_pass
    if not all_pass:
        print("Some test cases failed!", file=sys.stderr)
        sys.exit(2)
    else:
        print("Passed all test cases!")


def p2_runner(args):
  test_cases = [
    (["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"], "142"),
    (["5def6","ghij7klmnop2","qrst8uvwxyz0","12345"], "223"),
    (["9abc0","pqr3stu8vwx","zyxwvuts7rqp","654321"], "266"),
    (["1a2b3c4d5e6f7g8h9i0j","qrstuvwxyz12345"], "25"),
    (["0","123","4567","89"], "149"),
    (["a1b","c2d","e3f"], "66"),
    (["999","888","777","666"], "330"),
    (["3YR0th6FnmOVZ7p5KzEoCjD9WuGfivqIxPLGk4w8d2eUsb1aNrHlTMQyBcAJX",
      "7bKzfU1E0R2OgL8WJdXxPmrZitclhNkuaSD4pHn3vIjF9o6eGwQMVYCq5TsBAY",
      "8G1hsaJ7m5ZVefTcRbNWk6P0xd39DjyrE4vYKOM2LoAnqStXuzwUgBQIiCpFHL"], "188")
  ]

  check_all(args.program_exec, test_cases)
