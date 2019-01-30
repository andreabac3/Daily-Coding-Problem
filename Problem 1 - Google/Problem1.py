#!/usr/bin/env python3

def solve(arraylist, key):
    Set = set()
    for elem in arraylist:
        if elem > key:
            continue
        if (key - elem) in Set:
            return True
        Set.add(elem)
    return False


if __name__ == "__main__":
    list1 = [10, 15, 3, 7]
    k = 17
    print(solve(list1, k))
