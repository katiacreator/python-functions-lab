def sum_to(n):
  sum = 0
  for i in range(1, n+1, 1):
    sum += i
  return sum
print(sum_to(6))
print(sum_to(10))

def largest(list):
  list.sort()
  return list[-1]

print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))