CHAR_TO_DEC = {chr(dec): dec for dec in range(0, 127)}

if __name__ == "__main__":
    for char, dec in CHAR_TO_DEC.items():
        print(f"{char!r}: {dec}")
