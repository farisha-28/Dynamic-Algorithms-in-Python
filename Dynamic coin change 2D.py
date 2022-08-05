
def minCoin(n, list):
    total = len(list)
    table = [x for x in range(0,n)]

    for i in range(0,total):
        for j in range(0, n+1):




m = int(input())
coins = list(map(int, input.split()))
print(minCoin(m, coins))