def censor_python(wordsList: list[str])-> list[str]:
    return ['XXXXX' if item.lower() == 'python' else item for item in wordsList]





print(censor_python(["python", "hello", "HELLO"]))