
# def rodCut(len,values):
#     val = [-1 for item in range(0,len+1)]
#     val[0] = 0
#     max_value = float('-inf')
#     for i in range(0,len):
#         for j in range(0,i):
#             max_value = max(max_value, values[j-1] + val[i - j-1])
#             val[i] = max_value
#     return val[len]
#
#
#
# length = int(input())
# arr_values = list(map(int, input().split()))[:length]
# max_profit = rodCut(length,arr_values)
# print(max_profit)

INF = 100000;
r = [0] + [-1*INF]*5

def max(x, y):
  if x > y:
    return x
  return y

def bottom_up_rod_cutting(c, n):
  r = [0]*(n+1)
  r[0] = 0

  for j in range(1, n+1):
    maximum_revenue = -1*INF
    for i in range(1, j+1):
      maximum_revenue = max(maximum_revenue, c[i] + r[j-i])
    r[j] = maximum_revenue
  return r[n]

if __name__ == '__main__':
  #array starting from 1, element at index 0 is fake
  c = [0, 10, 24, 30, 40, 45]
  print(bottom_up_rod_cutting(c, 5))