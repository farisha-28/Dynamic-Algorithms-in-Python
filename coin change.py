
def currency(coinAr, val, c):
    ans = []

    for item in range(0, len(coinAr)):
        while val >= coinAr[item]:
            val -= coinAr[item]
            ans.append(coinAr[item])

        #     if mod == 0:
        #         return c
        #
        # coinAr[item] = -1
        # return currency(coinAr, mod, c)
    return ans


n = int(input())
coin = list(map(int, input().split()))[:n]
value = int(input())
coin.sort(reverse=True)
print(len(currency(coin, value, 0)))


