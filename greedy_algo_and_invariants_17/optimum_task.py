import collections
import sys
import random

# @include
PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))

def optimum_task_assignment(task_durations):
  task_durations.sort()
  return [PairedTasks(task_durations[i], task_durations[~i]) for i in range(len(task_durations) // 2)]