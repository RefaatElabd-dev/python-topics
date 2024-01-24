def first_non_repeating_char(text):
    chars_count = {}
    for i in text:
        chars_count[i] = int(chars_count.get(i) or 0) + 1
    for i in text:
        if (chars_count[i] == 1): 
            return i
    return None


print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""