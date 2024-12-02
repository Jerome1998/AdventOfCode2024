from typing import List

def is_valid(input: List[str]) -> bool:
  vc     
  
  return True

count = 0

with open("./02/input.txt", "r") as file:
  for line in file:
    split = line.split(" ")
    if is_valid(split):
      count += 1

print(count)