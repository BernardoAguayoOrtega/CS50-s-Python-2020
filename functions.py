# functions
from squares import square
import squares

print("---------------------------------------------")

for i in range(10):
  print(f"the square of {i} is {square(i)}")

print("---------------------------------------------")

for i in range(10):
  print(f"the square of {i} is {squares.square(i)}")