# def currency(arr, val, c):
#     for item in range(0, len(arr)):
#         if arr[item] <= val:
#             while val != 0:
#                 val = val - arr[item]
#             if val == 0:
#                 c += 1
#                 val = c
#     return c


n = int(input())
coin = list(map(int, input().split()))[:n]
for item in range(0,n+1):
    if item>=coin



value = int(input())
coin.sort(reverse=True)
print(currency(coin, value, 0))