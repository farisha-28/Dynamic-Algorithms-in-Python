def total_combination(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return total_combination(n - 1) + total_combination(n - 2)


no_of_stairs = int(input())
print(total_combination(no_of_stairs)+2)