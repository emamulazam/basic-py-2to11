alien_0 = {'color' : 'green' , 'points' : 5}
print(alien_0)

alien_0['x_position'] = 0   # adding items in dectionary
alien_0['y_position'] = 25  # adding items in dectionary
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'  # adding items in dectionary
alien_0['points'] = 5       # adding items in dectionary

print(alien_0)

del alien_0['points']       # removing items in dectionary

print(alien_0)

print("The alien is " + alien_0['color'] + '.')