def filter_strings_with_vowels(str_list: list[str])->list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [item for item in str_list if any(v in item for v in vowels)]

print(filter_strings_with_vowels(["apple", "banana", "zyxvb"]))