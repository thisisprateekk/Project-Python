import random
import time

# The project will prove that the binary search is always faster than naive search

# naive search: it scans the entire given list and compare if there is any element equal to the target
# if yes,it returns the index
# if no,then it returns "not found"
def naive_search(given_list, target):
    # example given_list  = [1, 3, 6, 5, 30]
    for i in range(len(given_list)):
        if given_list[i] == target:
            return i
    return "not found"


# binary search uses the method of divide and rule !
def binary_search(given_list, target, low=None, high=None):
    if low is None and high is None:
        low = 0
        high = len(given_list) - 1
    if high < low:
        return "not found"
    midpoint = (low + high) // 2

    # we'll check if l[midpoint] == target, and if not, we can find out if target will be to the left or right of midpoint
    # we know everything to the left of midpoint is smaller than the midpoint and everything to the right is larger than the midpoint

    if given_list[midpoint] == target:
        return midpoint
    elif target < given_list[midpoint]:
        return binary_search(given_list, target, low, midpoint-1)
    else:
        # target > l[midpoint]
        return binary_search(given_list, target, midpoint+1, high)

if __name__=='__main__':
    length = 10000
    # build a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start), "seconds")
    nst = end-start

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start), "seconds")
    bst = end-start
    diff = nst-bst
    print(f"the binary search is {diff} seconds faster than the naive search")

