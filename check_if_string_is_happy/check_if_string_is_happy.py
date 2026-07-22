def check_if_string_is_happy(word: str) -> bool:
    return all(a != b for a, b in zip(word, word[1:]))


print(check_if_string_is_happy("apple"))
      
    



