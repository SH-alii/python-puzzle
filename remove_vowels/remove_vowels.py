
def remove_vowels(input_str: str)-> str:
    list_vowel = ['a', 'e', 'i', 'o', 'u']
    for i in list_vowel:
     input_str = input_str.replace(i, '')
        
    return input_str



print(remove_vowels("Hello, World!"))