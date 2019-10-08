def find_nearest_repetition(paragraph):
  word_to_latest_index, nearest_repeated_distance = {}, float('inf')
  for i, word in enumerate(paragraph):
    if word in word_to_latest_index:
      latest_equal_word = word_to_latest_index[word]
      nearest_repeated_distance = min(nearest_repeated_distance, i - latest_equal_word)
    word_to_latest_index[word] = i
  return nearest_repeated_distance

def check_answer(s):
  return min([
    j - i for i, a in enumerate(s) for j, b in enumerate(s[i + 1:], i + 1)
    if a == b
  ],default=float('inf'))
A = ['foo', 'bar', 'widget', 'foo', 'widget', 'widget', 'adnan']
assert check_answer(A) == find_nearest_repetition(A)
A = ['foo', 'bar', 'widget', 'foo', 'xyz', 'widget', 'bar', 'adnan']
assert check_answer(A) == find_nearest_repetition(A)
A = ['foo', 'bar', 'widget', 'adnan']
assert check_answer(A) == find_nearest_repetition(A)
A = []
assert check_answer(A) == find_nearest_repetition(A)
A = ['foo', 'foo', 'foo']
assert check_answer(A) == find_nearest_repetition(A)