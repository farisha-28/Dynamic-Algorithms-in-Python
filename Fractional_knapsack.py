def knapsack(values, weights, capacity):
    values_by_items = []
    for items in range(0, len(weights)):
        values_by_items.append(values[items]/weights[items])
    combined_list = []
    inner = []
    for items in range(0, len(weights)):
        inner = [values[items], weights[items], values_by_items[items]]
        combined_list.append(inner)
    print(combined_list)
    combined_list.sort(key=lambda x: x[2], reverse=True)
    print(combined_list)

    profit = 0
    for items in range(0, len(combined_list)):
        print(f"remaining capacity = {capacity}")
        if capacity > 0 and combined_list[items][1] < capacity:
            profit += combined_list[items][0]
            print(f"{combined_list[items][0]} is added")
            capacity -= combined_list[items][1]
        else:
            break

    if capacity > 0:
        profit += combined_list[items][0] * (capacity/combined_list[items][1])
        print(f"{combined_list[items][0] * (capacity/combined_list[items][1])} is added")
    return profit


v = list(map(int, input().split()))
w = list(map(int, input().split()))
c = int(input())
res = knapsack(v, w, c)
print(res)

