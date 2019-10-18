from linked_list_prototype import ListNode

def merge_two_sorted_lists(L1, L2):
  # Creates a placeholder for the result.
  dummy_head = tail = ListNode()

  while L1 and L2:
    if L1.data < L2.data:
      tail.next, L1 = L1, L1.next
    else:
      tail.next, L2 = L2, L2.next
    tail = tail.next
  tail.next = L2 or L1
  return dummy_head.next
L1, L2 = None, None
assert merge_two_sorted_lists(L1, L2) is None

L1 = ListNode(123)
result = merge_two_sorted_lists(L1, L2)
assert result.data == 123 and result.next is None

L2 = ListNode(123)
L1 = None
result = merge_two_sorted_lists(L1, L2)
assert result.data == 123 and result.next is None

L1 = ListNode(-123)
L2 = ListNode(123)
result = merge_two_sorted_lists(L1, L2)
assert result.data == -123 and result.next.data == 123 and result.next.next is None