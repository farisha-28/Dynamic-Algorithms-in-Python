def currency(coinAr, m):
    ans = []

    for item in range(0, len(coinAr)):
        if m >= coinAr[item]:
            mod = m % coinAr[item]
            ans.append(m // coinAr[item])
            m = mod

            if m == 0:
                return ans


n = int(input())
coin = list(map(int, input().split()))[:n]
value = int(input())
coin.sort(reverse=True)
num = (currency(coin, value))

print(num)
print(sum(num))

