# Name: Jacob Chiasson
# Name of program: Q1 Counting
# Date of creation: June 1st 2022
# Purpose: Counting

number = int(input("Please enter a large number: "))
base = 0

while base < number:
  print(base)
  base = base + 1

while base == number:
  print(base)
  base = base -1

while base >= 0:
  print(base)
  base = base - 1