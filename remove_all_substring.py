def remove_all_substr(x,s):
    result = ''
    i = 0
    count = 0
    while i < len(s):
        if s[i:i+len(x)] == x:
            i = i + len(x)
        else:
            result = result + s[i]
            i = i + 1
    return result
    
          