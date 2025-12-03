from pkg.handle_test import run_solution as runner

def sol_p1(input):
    acc = 0
    for bank in input:
        first_digit = max(bank[:-1])
        second_digit = max(bank[bank.index(first_digit)+1:])
        acc += int(first_digit + second_digit)

    return acc

def sol_p2(input):
    acc = 0
    req_digits = 12
    for bank in input:
        digits = []
        last_index = 0
        for i in range(req_digits):
            curr = max(bank[last_index:(len(bank) - req_digits + i + 1)])
            last_index += (bank[last_index:(len(bank) - req_digits + i + 1)]).index(curr) + 1
            digits.append(curr)
        acc += int("".join(digits))
    return acc

runner(sol_p2, 3, '/testcases/2', '/q/q.txt')