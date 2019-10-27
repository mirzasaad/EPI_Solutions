def palindrome_partitioning(input):
  def directed_palindrome_partitioning(offset, partial_partition):
    if (offset == len(input)):
      result.append(list(partial_partition))
      return

    for i in range(offset + 1, len(input) + 1):
      prefix = input[offset:i]
      if prefix == prefix[::-1]:
        directed_palindrome_partitioning(i, partial_partition + [prefix])
  result = []
  directed_palindrome_partitioning(0, [])
  return result

# Pythonic solution uses bottom-up construction.
def palindrome_partitioning_pythonic(text):
  return ([[text[:i]] + right for i in range(1, len(text) + 1)
    if text[:i] == text[:i][::-1]
    for right in palindrome_partitioning_pythonic(text[i:])] or [[]])

result = palindrome_partitioning('abbbac')
v0 = ['a', 'b', 'b', 'b', 'a', 'c']
v1 = ['a', 'b', 'bb', 'a', 'c']
v2 = ['a', 'bb', 'b', 'a', 'c']
v3 = ['a', 'bbb', 'a', 'c']
v4 = ['abbba', 'c']
golden = [v0, v1, v2, v3, v4]
assert result == golden
assert palindrome_partitioning_pythonic('abbbac') == golden