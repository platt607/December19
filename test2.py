import sys
M = int(5)
N= int(input('get N:'))
count = -1
test = input("get numbers list:")
# convert strings to integers
numbers= test.split(',')
for i in range(0, len(numbers)):
  numbers[i]= int(numbers[i])

# Your code goes here


def divN(a,b) :
  if b%N:
    return(a * M)
  else:
    return(a)

map(divN,zip(numbers,range(len(numbers))))
print(numbers)


