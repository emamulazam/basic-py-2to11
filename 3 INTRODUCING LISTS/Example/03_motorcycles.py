motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)

motorcycle.append('ducati') # adds 'ducati' to the end of the list
print(motorcycle)


motor_cycles = []  # making a blank list

motor_cycles.append('honda')
motor_cycles.append('yamha')
motor_cycles.append('suzuki')
print(motor_cycles)

motor_cycles.insert(0, 'ducati') # adds "ducati" to the 0th positino
print(motor_cycles)

del motor_cycles[0] # delete 0th item
print(motor_cycles)