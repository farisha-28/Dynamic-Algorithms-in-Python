
def rodCut(len,values):
    a = [100][100]
    for i in range(0,len):
        for j in range(0,len):
            a[0][j] = 0
            a[i][0] = 0
            if i > j:
                a[i][j] = a[i-1][j]
            else:
                a[i][j] = max(a[i-1][j], values[i]+a[i-1][j])
    return a[i][j]


length = int(input())
arr_values = list(map(int, input().split()))[:length]
max_profit = rodCut(length,arr_values)
print(max_profit)