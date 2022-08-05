def knapSack(capacity, weight_list, value_list):
    n = len(value_list)
    table = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for items in range(n+1):
        for c in range(capacity+1):
            if items == 0 or c == 0:
                table[items][c] = 0
            elif weight_list[items-1] > c:
                table[items][c] = table[items - 1][c]
            else:
                table[items][c] = max(table[items - 1][c], value_list[items-1]
                                      + table[items][c - weight_list[items-1]])
    for items in range(0, len(table)):
        print(table[items])

    return table[n][capacity]


# val = [2, 3, 1, 4]
# wt = [3, 4, 6, 5]
# W = 8
val = list(map(int, input().split()))
wt = list(map(int, input().split()))
C = int(input())
inner = []
combined_list = []
for item in range(0, len(wt)):
    inner = val[item], wt[item]
    combined_list.append(inner)
combined_list.sort(key=lambda x: x[1])
v = []
w = []
for item in range(0, len(combined_list)):
    w.append(combined_list[item][1])
    v.append(combined_list[item][0])
print(combined_list)
print(knapSack(C, w, v))
