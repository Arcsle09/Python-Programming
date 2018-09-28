def powerset(lst):
  result = [[]]
  for i in lst:
    newsubset = [subset + [i] for subset in result]
    result.extend(newsubset)
  return result
