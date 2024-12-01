left = []
right = []

with open("./01/input.txt", "r") as file:
  for line in file:
    split = line.split("   ")
    left.append(int(split[0]))
    right.append(int(split[1]))

# left = [ 3, 4, 2, 1, 3, 3 ]
# right = [ 4, 3, 5, 3, 9, 3 ]

left.sort()
right.sort()

result = 0

for leftNumber in left:
  count = right.count(leftNumber)
  result += count * leftNumber

print(result)