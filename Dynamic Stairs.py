
def combination(n, st):
    if st[n] != -1:
        return st[n]
    else:
        st[n] = combination(n-1, st)+combination(n-2, st)
    return st[n]


n = int(input())
stairs = [-1 for i in range(0, n+1)]
stairs[0] = 0
stairs[1] = 1
m = combination(n,stairs)
print(m+2)