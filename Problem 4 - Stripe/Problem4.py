

def solve(arraylist):
    min = 10
    min2 = 10
    for elem in arraylist:
        if elem <= 0:
            continue
        if elem < min:
            min2 = min
            min = elem
        elif elem < min2:
            min2 = elem
    if min2 - min == 1:
        return min2 + 1
    elif min2 - min > 1:
        return min + 1


list1 = [3, 4, -1, 1]
list2 = [1, 2, 0]

print(solve(list1))
print(solve(list2))
