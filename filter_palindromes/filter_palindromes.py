

def filter_palindromes(wordList: list[str])->list[str]:
     return [item for item in wordList if(item == item[::-1])]
 
 
 
print(filter_palindromes(["cat", "dog", "racecar", "deified", "giraffe"]))