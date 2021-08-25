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

def occurances(str1, str2):
  #s.count(x)
  return str1.count(str2)

print(occurances('fleep floop', 'e'))
print(occurances('fleep floop', 'p'))
print(occurances('fleep floop', 'ee'))
print(occurances('fleep floop', 'fe'))

def product(*args):
  product = 1
  for n in args:
    product *= n
  return product

print(product(-1, 4)) # returns -4
print(product(2, 5, 5)) # returns 50
print(product(4, 0.5, 5)) # returns 10.0