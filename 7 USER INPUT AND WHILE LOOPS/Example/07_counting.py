current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue       # continue send reader to the start of the loop
    print(current_number)
  