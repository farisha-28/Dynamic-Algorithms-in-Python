
def rodCut(len,values):
    max_val = float('-inf')
    if len==0:
        return 0
    else:
        for i in range(0, len):
            max_val = max(max_val,values[i] + rodCut(len-i-1,values))
    return max_val


length = int(input())
arr_values = list(map(int, input().split()))[:length]
max_profit = rodCut(length,arr_values)
print(max_profit)