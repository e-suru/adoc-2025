from pkg.handle_test import run_solution as runner
from heapq import heappush, heappop
def sol_1(input):
    fresh_set = set()
    split_ind = input.index("")
    fresh_list = input[:split_ind]
    ids = input[split_ind+1:]

    for fresh_range in fresh_list:
        start, end  = fresh_range.split('-')
        for i in range(int(start), int(end) + 1):
            fresh_set.add(int(i))
    acc = 0
    for i in ids:
        i = int(i)
        if i in fresh_set:
            acc += 1
    
    return acc

def sol_1_attempt_2(input):
    fresh_sorted = []
    split_ind = input.index("")
    fresh_ranges = input[:split_ind]
    ids = map(lambda id: int(id), input[split_ind+1:])

    def make_fresh_sorted(fresh_ranges):
        fresh_sorted = []
        for f_range in fresh_ranges:
            print(fresh_sorted)
            start, end = map(lambda x: int(x), f_range.split('-'))
            for i in range(len(fresh_sorted)):
                prev_interval = fresh_sorted[i]
                print("considering", (start, end))
                print("END INTERVAL", prev_interval[1])
                print("comparison", prev_interval[1] >= end)
                if prev_interval[0] <= start and prev_interval[1] >= end:
                    # new range already encapsulated in existing range
                    break
                elif prev_interval[0] <= start and prev_interval[1] < end:
                    # start is after prev_interval.start, end is after prev_interval.end
                    if start <= prev_interval[1]:
                        j = i + 1
                        to_remove = [prev_interval]
                        new_interval = (prev_interval[0], end)
                        print("new int", new_interval)
                        while j < len(fresh_sorted) and (fresh_sorted[j][0] <= prev_interval[1]) and (fresh_sorted[j][1] >= prev_interval[1]):
                            print("yarr")
                            new_interval = (prev_interval[0], fresh_sorted[j][1])
                            to_remove.append(fresh_sorted[j])
                            j += 1
                        print("b4 delete", fresh_sorted)
                        for _ in range(i, j):
                            del fresh_sorted[i]
                            ##heappop(fresh_sorted, k)
                        heappush(fresh_sorted, new_interval)
                        print("after delete", fresh_sorted)
                        break
                else:
                    # start smaller than current interval - haven't found interval
                    continue
            # if reached end of list and no overlapping interval
            print("adding", (start, end))
            print("curr q", fresh_sorted)
            heappush(fresh_sorted, (start, end))
        return fresh_sorted
    
    def check_ids(ids, fresh_sorted):
        acc = 0
        for id in ids:
            print("id", id)
            for i in range(len(fresh_sorted)):
                print("considering", fresh_sorted[i])
                if id > fresh_sorted[i][1]:
                    continue
                elif id > fresh_sorted[i][0] and id < fresh_sorted[i][1]:
                    print("range added", fresh_sorted[i][0])
                    acc += 1
                else:
                    break
        return acc
        
    fresh_sorted = make_fresh_sorted(fresh_ranges)
    return check_ids(ids, fresh_sorted)


runner(sol_1_attempt_2, 5, '/testcases/1', '/q/q.txt')