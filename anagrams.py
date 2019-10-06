import collections

# @include
def find_anagrams(dictionary):
  sorted_string_to_anagrams = collections.defaultdict(list)
  for s in dictionary:
    # Sorts the string, uses it as a key, and then appends the original string as another value into hash table.
    sorted_string_to_anagrams[''.join(sorted(s))].append(s)
  return [group for group in sorted_string_to_anagrams.values() if len(group) > 1]

D = ['debit card', 'bad credit', 'the morse code', 'here come dots', 'the eyes', 'they see', 'THL']
result = find_anagrams(D)

# 3 nontrivial groups:
# ['debit card', 'bad credit'],
# ['the morse code', 'here come dots']
# ['the eyes',     'they see']
# Since the string 'THL' has no anagrams in D, the result
# contains 3 entries
assert len(result) == 3