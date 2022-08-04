
choices = int(input())
price = list(map(int, input().strip().split()))
l = len(price)
remaining_days = list(map(int, input().strip().split()))
value = 0

profit_per_chip = sorted([[price[item]/remaining_days[item],remaining_days[item]] for item in range(0,len(price))], reverse=True)
print(profit_per_chip)
while choices>0 and l>0:
    maxi = 0
    idx = None
    for i in range(l):
        if profit_per_chip[i][1] > 0 and maxi < profit_per_chip[i][0]:
            maxi = profit_per_chip[i][0]
            idx = i

    if idx is None:
        print(0)

    if profit_per_chip[idx][1] <= choices:
        value += profit_per_chip[idx][0] * profit_per_chip[idx][1]
        choices -= profit_per_chip[idx][1]
    else:
        if profit_per_chip[idx][1] > 0:
            value += (choices / profit_per_chip[idx][1]) * profit_per_chip[idx][1] * profit_per_chip[idx][0]
            print(value)
    profit_per_chip.pop(idx)
    choices -= 1
print(value)







