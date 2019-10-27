def generate_power_set(input_set):
  # Generate all subsets whose intersection with input_set[0], ...,
  # input_set[to_be_selected - 1] is exactly selected_so_far.
  def directed_power_set(to_be_selected, selected_so_far):
    if to_be_selected == len(input_set):
      power_set.append(list(selected_so_far))
      return
    
    directed_power_set(to_be_selected + 1, selected_so_far + [input_set[to_be_selected]])
    directed_power_set(to_be_selected + 1, selected_so_far)

  power_set = []
  directed_power_set(0, [])
  return power_set

assert generate_power_set(['a', 'b', 'c']) == [['a', 'b', 'c'], ['a', 'b'], ['a', 'c'], ['a'], ['b', 'c'], ['b'], ['c'], []]