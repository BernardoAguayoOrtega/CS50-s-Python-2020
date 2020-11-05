from sys import exit

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: only acepts numbers")
    exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    exit(1)

print(f"{x} / {y} = {result}")
