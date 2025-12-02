from pkg.handle_test import run_solution as runner

def solution_pt1(input):
    acc = 50
    counter = 0
    for i in input:
        direction = i[:1]
        val = int(i[1:]) % 100
        if direction == 'L':
            acc -= val
        else:
            acc += val
        
        if acc < 0:
            acc += 100
        elif acc > 99:
            acc -= 100
        if acc == 0:
            counter += 1
    return counter

def solution_pt2(input):
    prev_acc = 50
    acc = 50
    counter = 0
    for i in input:
        direction = i[:1]
        counter += int(i[1:]) // 100
        val = int(i[1:]) % 100
        if direction == 'L':
            acc -= val
        else:
            acc += val
        
        if acc < 0:
            acc += 100
            if not prev_acc == 0:
                counter += 1
        elif acc > 99:
            acc -= 100
            if not prev_acc == 0:
                counter += 1
        elif acc == 0:
            counter += 1
        prev_acc = acc
    return counter

runner(solution_pt2, 1, '/testcases/2', '/q/0.txt')