from pkg.handle_test import run_solution as runner

def sol_p1(input):
    ranges = input[0].split(',')
    acc = 0
    for r in ranges:
        start, end = r.split('-')
        for i in range(int(start), int(end)+1):
            if len(str(i)) % 2 == 1:
                continue
            middle_ind = len(str(i)) // 2
            if not int(middle_ind) == middle_ind:
                continue
            i_string = str(i)
            if i_string[:middle_ind] == i_string[middle_ind:]:
                acc += i
    return acc

def sol_p2(input):
    ranges = input[0].split(',')
    acc = 0
    for r in ranges:
        start, end = r.split('-')
        for i in range(int(start), int(end)+1):
            i_string = str(i)
            for j in range(1, len(i_string)//2 + 1):
                if not len(i_string) % j == 0:
                    continue
                substr = i_string[:j]
                check_ind = j
                repeat_flag = True
                while check_ind < len(i_string):
                    if not i_string[check_ind:check_ind + j] == substr:
                        repeat_flag = False
                        break
                    check_ind += j
                if repeat_flag:
                    acc += i
                    break
    return acc
                    
                
runner(sol_p2, 2, '/testcases/2', '/q/q.txt')