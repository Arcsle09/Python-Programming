#possible permutations and Unique possible combinations of a given set 
def perm_comb(n):
  n = list(n)
  lst = [({x,y}) for x in n for y in n]
  
  for x in n:
    if {x} in lst:
      lst.remove({x})
  print("The permutations are: ",lst)
  
  print(end = "\n")

  fin_list = []
  for y in lst:
    if y not in fin_list:
      fin_list.append(y)
  print("The unique possible combinations are:",fin_list)
