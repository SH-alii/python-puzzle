

def get_longest_string(list: list[str]) -> str:
    longest_word = ''
    
    for i in list:
      
        if( len(i) > len(longest_word)): 
            longest_word = i
    
    return longest_word

print(get_longest_string(["a", "b", "c", "d"]))