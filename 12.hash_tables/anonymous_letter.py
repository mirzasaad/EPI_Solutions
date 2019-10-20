from collections import Counter

def is_letter_constructible_from_magazine(letter_text, magazine_text):
  # Compute the frequencies for all chars in letter_text.
  char_frequency_letters = Counter(letter_text)

  # Checks if characters in magazine_text can cover characters in char_frequency_letters
  for c in magazine_text:
    if c in char_frequency_letters:
      char_frequency_letters[c] -= 1
      if char_frequency_letters[c] == 0:
        del char_frequency_letters[c]
        if not char_frequency_letters:
          # all characters are accounted for in letter
          return True
  # Empty char_frequency_for_letter means every char in letter_text can be covered by a character in magazine_text. 
  return not char_frequency_letters

def is_letter_constructible_from_magazine_pythonic(letter_text, magazine_text):
  return (not Counter(letter_text) - Counter(magazine_text))

assert not is_letter_constructible_from_magazine('123', '456')
assert not is_letter_constructible_from_magazine('123', '12222222')
assert is_letter_constructible_from_magazine('123', '1123')
assert is_letter_constructible_from_magazine('123', '123')
assert is_letter_constructible_from_magazine('GATTACA',
                                              'A AD FS GA T ACA TTT')
assert not is_letter_constructible_from_magazine('a', '')
assert is_letter_constructible_from_magazine('aa', 'aa')
assert is_letter_constructible_from_magazine('aa', 'aaa')
assert is_letter_constructible_from_magazine('', '123')
assert is_letter_constructible_from_magazine('', '')

assert not is_letter_constructible_from_magazine_pythonic('123', '456')
assert not is_letter_constructible_from_magazine_pythonic('123', '12222222')
assert is_letter_constructible_from_magazine_pythonic('123', '1123')
assert is_letter_constructible_from_magazine_pythonic('123', '123')
assert is_letter_constructible_from_magazine_pythonic(
    'GATTACA', 'A AD FS GA T ACA TTT')
assert not is_letter_constructible_from_magazine_pythonic('a', '')
assert is_letter_constructible_from_magazine_pythonic('aa', 'aa')
assert is_letter_constructible_from_magazine_pythonic('aa', 'aaa')
assert is_letter_constructible_from_magazine_pythonic('', '123')
assert is_letter_constructible_from_magazine_pythonic('', '')