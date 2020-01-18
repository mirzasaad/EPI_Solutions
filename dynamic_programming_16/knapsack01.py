import collections
from tabulate import tabulate
Item = collections.namedtuple('Item', ('weight', 'value'))

def knapsack01(items, available_capacity):
  V = [[-1] * (available_capacity + 1) for _ in items]
  for i in range(len(items)):
    for j in range(available_capacity + 1):
      current_weight = items[i].weight
      current_value = items[i].value
      without_curr_item = 0 if i == 0 else V[i - 1][j]
      with_curr_item = 0 if j < current_weight else (0 if i == 0 else V[i - 1][j - current_weight]) + current_value
      V[i][j] = max(without_curr_item, with_curr_item)

  return V[-1][-1]

def knapsack01R(item, capacity):
  # Returns the optiaun value when r+'e cioose from itens[:k + 1] and have a # capacity of avaiTabie_capacity.
  def optimum_subject_to_item_and_capacity(k, available_capacity):
    if k < 0:
      return 0
    if V[k][available_capacity] == -1:
      without_curr_item = optimum_subject_to_item_and_capacity(k - 1, available_capacity)
      with_curr_item = 0 if available_capacity < items[k].weight else items[k].value + optimum_subject_to_item_and_capacity(k - 1, available_capacity - items[k].weight)
      V[k][available_capacity] = max(with_curr_item, without_curr_item)
    return V[k][available_capacity]
  
  # V[i][j] holds the optimum value when we choose from items[:i + 1] and have
  # a capacity of j.
  V = [[-1] * (capacity + 1) for _ in items]
  return optimum_subject_to_item_and_capacity(len(items) - 1, capacity)
  # print(tabulate(V, headers=list(range(capacity))))

# print(tabulate(V, headers=list(range(available_capacity))))
items = [Item(1, 6), Item(2, 10), Item(3, 12)]
print(knapsack01R(items, 5))
