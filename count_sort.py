def basic_counting_sort(tlist, k):
  """ Counting sort algo. Modified existing list. Only for positive integer.
    Args:
      tlist: target list to sort
      k: max value assume known before hand
    Disadv:
      It only does for positive integer and unable to handle more complex sorting (sort by str, negative integer etc)
      It straight away retrieve all data from count_list using count_list index as its ordering.
      Do not have the additional step to modify count_list to capture the actual index in output.
  """
 
  # Create a count list and using the index to map to the integer in tlist.
  count_list = [0]*(k)

  # loop through tlist and increment if exists
  for num in tlist:
    count_list[num] = count_list[num] + 1
  # Sort in place, copy back into original list
  write_index = 0
  for i in range(len(count_list)):
    while count_list[i] > 0:
      tlist[write_index] = i
      write_index += 1
      count_list[i] -= 1
      
def get_sortkey(n):
  """ Define the method to retrieve the key """
  return n
 
def counting_sort(tlist, k, get_sortkey):
  """ Counting sort algo with sort in place.
      Args:
          tlist: target list to sort
          k: max value assume known before hand
          get_sortkey: function to retrieve the key that is apply to elements of tlist to be used in the count list index.
          map info to index of the count list.
      Adv:
          The count (after cum sum) will hold the actual position of the element in sorted order
          Using the above, 

  """
 
  # Create a count list and using the index to map to the integer in tlist.
  count_list = [0]*(k)

  # iterate the tgt_list to put into count list
  for n in tlist:
    count_list[get_sortkey(n)] = count_list[get_sortkey(n)] + 1 

  # Modify count list such that each index of count list is the combined sum of the previous counts
  # each index indicate the actual position (or sequence) in the output sequence.
  for i in range(k):
    if i ==0:
      count_list[i] = count_list[i]
    else:
      count_list[i] += count_list[i-1]

  output = [None]*len(tlist)
  for i in range(len(tlist)-1, -1, -1):
    sortkey = get_sortkey(tlist[i])
    output[count_list[sortkey]-1] = tlist[i]
    count_list[sortkey] -=1

  return output
 
A = [1, 4, 6, 3]
A = counting_sort(A, 6 + 1, get_sortkey)
print(A)