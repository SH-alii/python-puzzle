

def string_to_ascii(text: str)->list[int]:
    char = {chr(dec): dec for dec in range(0,128)}
    return [char[ch] for ch in text  ]


def ascii_to_string(list_ascii: list[int])-> str:
    asci = {dec: chr(dec) for dec in range(0,128) }
    return "".join(asci[dec] for dec in list_ascii)


print(string_to_ascii("Programming puzzles!"))
print(ascii_to_string(string_to_ascii("Programming puzzles!")))