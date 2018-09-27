def remove_dups(s):
#will remove duplicates of the given string
  result = ''
  for i in s:
    if not(i in result):
      result = result + i
  return result

