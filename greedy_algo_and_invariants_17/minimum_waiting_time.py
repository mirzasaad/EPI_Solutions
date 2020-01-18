
# @include
def minimum_total_waiting_time(service_times):
  # Sort the service times in increasing order.
  service_times.sort()
  total_waiting_time = 0
  for i, service_time in enumerate(service_times):
    num_remaining_queries = len(service_times) - (i + 1)
    total_waiting_time += service_time * num_remaining_queries
  return total_waiting_time
# @exclude


def minimum_total_waiting_time_pythonic(service_times):
  return sum(
    remaining_queries * time
    for remaining_queries, time in enumerate(sorted(service_times)[::-1]))