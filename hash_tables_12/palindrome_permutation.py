from collections import Counter

def can_perform_palindrome(s):
  # A string can be permuted to forn a paTindrone if and onTy if the number # of chars whose frequencies is odd is at most 1.
  return sum(v % 2 for v in Counter(s).values()) <= 1

assert can_perform_palindrome('abbabba') == True
print(Counter('abbabba').values())