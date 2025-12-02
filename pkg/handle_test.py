import argparse
from pathlib import Path

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_parser():
    parser = argparse.ArgumentParser(prog="Advent of Code 2025 solution")
    parser.add_argument('-t', '--test', action='store_true')
    parser.add_argument('-p', '--printtest', action='store_true')
    return parser

def run_solution(solution, num, t_files, q_file):
    parser = get_parser()
    args = parser.parse_args()
    if (args.test):
        counter = 0
        passed = 0
        for test in Path(str(num) + t_files).iterdir():
            if test.is_file():
                full_test = test.read_text().split("\n")
                answer = full_test.pop()
                sol_answer = str(solution(full_test))
                if (args.printtest):
                    print(f"{bcolors.BOLD} Test {counter}:{bcolors.ENDC} {full_test}")
                if (answer == sol_answer):
                    passed += 1
                    print(f"{bcolors.OKGREEN}Passed test case {counter}{bcolors.ENDC}")
                else:
                    print(f"{bcolors.FAIL}Failed test case {counter} - expected {answer}, got {sol_answer}{bcolors.ENDC}")
                counter += 1
        print(f"Passed {passed}/{counter} tests")
    else:
        with Path(str(num) + q_file).open() as f:
            q_input = f.read().split("\n")
            answer = solution(q_input)
            print(f"Answer: {answer}")
