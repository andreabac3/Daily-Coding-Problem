#!/usr/bin/env python3

def solve(arraylist):
    min1 = float("inf")
    min2 = float("inf")
    for elem in arraylist:
        if elem <= 0:
            continue
        if elem < min1:
            min2 = min1
            min1 = elem
        elif elem < min2:
            min2 = elem
    if min2 - min1 == 1:
        return min2 + 1
    elif min2 - min1 > 1:
        return min1 + 1

if __name__ == "__main__":
    list1 = [3, 4, -1, 1]
    list2 = [1, 2, 0]

    print(solve(list1))
    print(solve(list2))
