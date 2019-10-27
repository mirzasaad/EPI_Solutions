from linked_list_prototype import ListNode
from merge_two_sorted_lists import merge_two_sorted_lists

def stable_sort(L):
  if not L or not L.next:
    return L
  pre_slow, slow, fast = None, L, L
  while fast and fast.next:
    pre_slow = slow
    slow, fast = slow.next, fast.next
  pre_slow.next = None
  return merge_two_sorted_lists(stable_sort(L), stable_sort(slow))

L = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, None)))))
stable_sort(L)
print(L)