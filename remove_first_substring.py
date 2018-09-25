def remove_first_substr(x,s):
    result = ''
    i = 0
    count = 0
    while i < len(s):
        if s[i:i+len(x)] == x and count < 1:
            i = i + len(x)
            count = count + 1 
        else:
            result = result + s[i]
            i = i + 1
    return result