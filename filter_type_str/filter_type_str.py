


def filter_type_str(inputList : list[str | int]):
     return [s for s in inputList if(isinstance(s, str))]
 
 
 
 
print(filter_type_str(["www", 112, 22, 'ff', '3']))