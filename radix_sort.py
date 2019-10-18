from functools import partial
import random
from count_sort import counting_sort
def get_sortkey2(n, digit_place=2):
  """ Define the method to retrieve the key
      return the key based on the digit place. Current set base to 10
  """
  return (n//10**digit_place)%10

## Create random list for demo counting sort.
random.seed(1)
tgt_list = [random.randint(20,400) for n in range(10)]
print("Unsorted List")
print(tgt_list)
 
## Perform the counting sort.
print("\nSorted list using counting sort")
 
output = tgt_list
for n in range(3):
  output = counting_sort(output, 30, partial(get_sortkey2, digit_place=n))
  print(output)
 