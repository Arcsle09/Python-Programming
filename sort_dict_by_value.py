
# Write a script to sort a dictionary according to Value

first_dict = dict()
n = int(input("How many items you need in a list: "))

for i in range(0,n):
  name = input("Enter the name: ")
  age = int(input("Enter the age: "))
  first_dict[name] = age

print("The list of Youngest to Oldest People:")
for i in sorted(first_dict.values()):
  print(list(first_dict.keys())[list(first_dict.values()).index(i)],":",i)

