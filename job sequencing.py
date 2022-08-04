
choice = int(input())
chips = [[input(), int(input()), int(input())] for item in range(0, choice)]
length = len(chips)
n = int(input())
s = 0
for i in range(length):
    for j in range(length - 1 - i):
        if chips[j][2] < chips[j + 1][2]:
            chips[j], chips[j + 1] = chips[j + 1], chips[j]

result = [False] * n

ch = ['-1'] * n
for i in range(length):
    for j in range(min(n - 1, chips[i][1] - 1), -1, -1):

        if result[j] is False:
            result[j] = True
            ch[j] = chips[i][0]
            break

for(obj, deadLine, price) in chips:
    for it in ch:
        if obj == it:
            s += price
print(ch)
print(s)
