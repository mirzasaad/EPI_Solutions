from linked_list_prototype import ListNode

# @include
def insertion_sort(L):
  dummy_head = ListNode(0, L)

  while L and L.next:
    if L.data > L.next.data:
      target, pre = L.next, dummy_head
      while pre.next.data < target.data:
        pre = pre.next
      temp, pre.next, L.next = pre.next, target, target.next
      target.next = temp
    else:
      L = L.next
  return dummy_head.next

L = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, None)))))

result = insertion_sort(L)
def insertion_sort_array(A):
  for index in range(1, len(A)):
    currentValue = A[index]
    position = index
    while position > 0 and A[position - 1] > currentValue:
      A[position] = A[position - 1]
      position -= 1
    A[position] = currentValue
  return A

A = [5,2,1,9,0,4,6]
A = insertion_sort_array(A)