import collections
def find_all_substrings(s, words):
  def match_all_words_in_dict(start):
    curr_string_to_freq = collections.Counter()
    for i in range(start, start + len(words) * unit_size, unit_size):
      curr_word = s[i:i+unit_size]
      it = word_to_freq[curr_word]
      if it == 0:
        return False
      curr_string_to_freq[curr_word] += 1
      if curr_string_to_freq[curr_word] > it:
        # curr_word occurs too many times for a match to be possible.
        return False
    return True

  word_to_freq = collections.Counter(words)
  unit_size = len(words[0])
  length = len(s) - unit_size * len(words)
  return [
    i for i in range(length + 1)
    if match_all_words_in_dict(i)
  ]

s = 'barfoothefoobarman'
result = find_all_substrings(s, ['foo', 'bar'])
assert result == [0, 9]
s = 'dcacdabcd'
result = find_all_substrings(s, ['cd', 'ab'])
assert result == [3, 5]