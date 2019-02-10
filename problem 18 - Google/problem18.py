#!/bin/python3

'''
Two type of solution,
    1) Solve using the Python slices without using extra space,
    2) Solve using a mod 3 counter and O(k) space
'''


def solve(arr):
    for i in range(len(arr) - 2): print(arr[i: i + 3], max(arr[i:i + 3]))


def solve2(arr):
    x = lista[:3]
    print(x, max(x))
    cnt = 0
    for i in range(3, len(arr)):
        x[cnt] = arr[i]
        print(x, max(x))
        cnt = (cnt + 1) % 3


lista = [10, 5, 2, 7, 8, 7]
solve(lista)
solve2(lista)
