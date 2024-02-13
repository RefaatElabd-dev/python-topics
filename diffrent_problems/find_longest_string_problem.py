def find_longest_string(strings):
    max_length_string = ''
    for word in strings:
        if len(word) > len(max_length_string):
            max_length_string = word
    return max_length_string


string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""