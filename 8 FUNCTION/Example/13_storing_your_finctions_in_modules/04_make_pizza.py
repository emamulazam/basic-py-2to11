# Using as to Give a Function an Allias
# You'll give the function this special nickname when you import the function

from pizza_01 import make_pizza as mp
# from module_name import function_name as fn
mp(16, "pepperoni")
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

#--------------------------------------------------------------------------------------

# Using as to Give a Module an alias
import pizza_01 as p
# import module_name as mn
p.make_pizza(16, "pepperoni")
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
