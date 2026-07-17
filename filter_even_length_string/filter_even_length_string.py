
def get_lenth_value(string: str)-> int:
    return len(string)



def filter_even_length_strings(list: list[str])->list[str]:
    if not list:
        return []
    shortest = min(len(s) for s in list)
    return [s for s in list if len(s) == shortest]



print(filter_even_length_strings(["cat", "dog", "fish", "elephant"]))