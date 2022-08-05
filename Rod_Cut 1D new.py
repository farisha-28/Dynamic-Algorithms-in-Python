def rodCut(price, n):

    T = [0] * (n + 1)
    max_value = float('-inf')
    # >> > [0] * 10
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(1, n + 1):
        # divide the rod of length `i` into two rods of length `j`
        # and `i-j` each and take maximum
        for j in range(1, i + 1):
            max_value = max(max_value, price[j - 1] + T[i - j])
            T[i] = max_value

    return T[n]


price = list(map(int, input().split()))
n = int(input())

print("Profit is", rodCut(price, n))