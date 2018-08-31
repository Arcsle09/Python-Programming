# program to prove "==" is not same as "is" 

# In python, the variable acts like an object.

# It can be compared with pointer in C programming. 

# the variable(or object) stores the memory address of value being stored inside of memory. 

x = 42

y = 42.0 

#x == y
#Out[327]: True

#x is y
#Out[328]: False 

#the variable makes a decision based on the data type of the values. 

# If the same values have same data type,
        # then both x and y variables will reference to the same memory address.
#  else
        # x and y will point different memory addresses and hence different values.

