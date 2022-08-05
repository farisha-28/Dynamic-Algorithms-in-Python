def coin_change(change, coins_list):
    n = len(coins_list)
    table = [[x for x in range(change + 1)] for x in range(n)]
    print(table)

    for items in range(0, n):
        for j in range(0, change+1):
            if j == 0:
                table[items][j] = 0
            elif coins_list[items] > j:
                table[items][j] = table[items - 1][j]
            else:
                table[items][j] = min(table[items-1][j], 1+table[items][j-coins_list[items]])
    for items in range(0, len(table)):
        print(table[items])

    return table[n-1][change]


coins = list(map(int, input().split()))
change_amount = int(input())
print(coin_change(change_amount, coins))

