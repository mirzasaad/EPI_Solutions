import sys
import collections
import string
import random

# @include
Person = collections.namedtuple('Person', ('age', 'name'))

def group_by_age(people):
  age_to_count = collections.Counter([p.age for p in people])
  age_to_offset, offset = {}, 0
  for age, count in age_to_count.items():
    offset += count
    age_to_offset[age] = offset - 1
    
  while age_to_offset:
    from_age = next(iter(age_to_offset))
    from_idx = age_to_offset[from_age]
    to_age = people[from_idx].age
    to_idx = age_to_offset[to_age]
    people[to_idx], people[from_idx] = people[from_idx], people[to_idx]
    age_to_count[to_age] -= 1
    if age_to_count[to_age]:
      age_to_offset[to_age] -=1
    else:
      del age_to_offset[to_age]
  return people
  
people = [
        Person(20, 'foo'), Person(10, 'bar'), Person(20, 'widget'),
        Person(20, 'something')
    ]
group_by_age(people)
if people[0].age == 10:
  assert people[1].age == 20 and people[2].age == 20 and people[
        3].age == 20
else:
  assert people[1].age == 20 and people[2].age == 20 and people[
        3].age == 10