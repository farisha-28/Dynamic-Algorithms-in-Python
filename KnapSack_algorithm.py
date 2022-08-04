
objects = int(input())
bag_capacity = int(input())
profits = list(map(int, input().split()))[:objects]
weights = list(map(int, input().split()))[:objects]
sack = []

for item in range(0, objects):
    ratio = profits[item]/weights[item]
    sack.append([ratio, weights[item], profits[item]])

print(sack)
sack.sort(reverse=True)
print(sack)

profit_sum = 0

for item in range(0, len(sack)):
    if bag_capacity > 0 and sack[item][1] <= bag_capacity:
        bag_capacity = bag_capacity-sack[item][1]
        profit_sum += sack[item][2]
    else:
        break
if bag_capacity > 0 :
        profit_sum += sack[item][2]*(bag_capacity/sack[item][1])


print(profit_sum)




