def total_combination(n):

    stairs = [0, 1]

    for i in range(2, n + 1):
        stairs.append(stairs[i - 1] + stairs[i - 2])
    return stairs[n]


no_of_stairs = int(input())
print(total_combination(no_of_stairs)+2)