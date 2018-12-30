# -*- coding: utf-8 -*-
"""

Prpblem Statement:
Using a class employee,
1. create a list of employees(data taken from users)
2. display list of employees in sorted order according to their names.
3. Define a function to sort list of employees according to their salary  in descending order. 

@author: Rakesh
""" 

class employee:
    def __init__(self):
        self.empid = int(input('Enter the empid: '))
        self.name = (input('Enter the name: '))
        self.salary = int(input('Enter the salary: '))   
 
    def append_data(self):
         employee_list.append(self.empid)
         employee_list.append(self.name)
         employee_list.append(self.salary)
    
    #create chunks of sublists from original list. 
    def chunks(l, n):
    # For item i in a range that is a length of l
        for i in range(0, len(l), n):
        # Create an index range for l of n items:
            yield l[i:i+n] 

#entering the number of employee records
n = int(input('how many employee data you would like to record?')) 

#initializing the list of employees
employee_list = []        

#creating the list of variables to be assigned during instantiation of class
obj = ["obj_%d" % x for x in range(n)] 

#creates objects and produces the list of employee data 
for i in range(n):
    print('Enter the details of employee - ',i+1)
    obj[i] = employee()
    obj[i].append_data()
 
print('The sorted list by name:')
sorted_list_by_name = sorted(list(employee.chunks(employee_list,3)), key = lambda x: x[1])
print(sorted_list_by_name)

print('The sorted list by salary in descending order:')      
sorted_list_by_salary = sorted(list(employee.chunks(employee_list,3)),reverse=True,key = lambda x: x[2])
print(sorted_list_by_salary)
        
