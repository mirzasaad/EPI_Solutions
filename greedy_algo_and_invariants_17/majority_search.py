import random
import string

def rand_string(length):
  return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def majority_search(input_stream):
  candidate, candidate_count = None, 0
  for it in input_stream:
    if candidate_count == 0:
      candidate, candidate_count = it, candidate_count + 1
    elif candidate == it:
      candidate_count += 1
    else:
      candidate_count -= 1
  return candidate

n = random.randint(1, 10)
stream = [rand_string(random.randint(1, 5)) for _ in range(n)]
# generate the majority
stream += [stream[-1]] * n
stream += [stream[0]] * 2

assert majority_search(iter(stream)) == stream[-3]