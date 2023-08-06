
my_list = []

my_list.append("Bing")

my_list.insert(0, 42)

my_list.extend([True, False])

my_list.append(("red", "green", "blue"))

my_list.append({1, 2, 3})

my_list.append({"name": "Alice", "age": 25})

print(my_list)




my_list = [10, 20, 30, 40, 50]

def swap_first_last(lst):
  first = lst[0]
  lst[0] = lst[-1]
  lst[-1] = first
  return lst

print(swap_first_last(my_list)) # [50, 20, 30, 40, 10]

def sum_digits(lst):
  total = 0
  for num in lst:
    for digit in str(num):
      total += int(digit)
  return total

print(sum_digits(my_list)) # 8

def min_element(lst):
  minimum = lst[0]
  for num in lst[1:]:
    if num < minimum:
      minimum = num
  return minimum

print(min_element(my_list)) # 10



my_dict = {"a": 10, "b": 20, "c": 30}

def sort_by_key(d):
  items = list(d.items())
  items.sort(key=lambda x: x[0])
  return dict(items)

print(sort_by_key(my_dict)) 

def sum_values(d):
  total = 0
  for value in d.values():
    total += value
  return total

print(sum_values(my_dict)) # 60

def sort_by_value_desc(d):
  items = list(d.items())
  items.sort(key=lambda x: x[1], reverse=True)
  return dict(items)

print(sort_by_value_desc(my_dict))
