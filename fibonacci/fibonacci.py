
def fibonacci(squence: int)-> list[int]:
   

     if(squence == 0):
         return []
     if(squence == 1):
         return [1]
     if(squence == 2):
         return[0, 1]
   
     print(squence)
     
     numbers = fibonacci(squence - 1)
     numbers.append(numbers[-1] + numbers[-2])
     print(numbers)
     return numbers
     
     
     
#fibonacci(8)



def countdown(n : int):
    if n <= 0:
        return
    print(n)
    countdown( abs(n -1) )
    


#countdown(5)


def count_up(n: int):
    if n <= 0:
        return
    count_up(n -1)
    print(n)
    return

#count_up(100)


def sum_to(sum: int) -> int:
    if sum == 1:
        return 1

    print(sum)
    return sum + sum_to(abs(sum - 1))

#print(sum_to(5))
    


def factorial(fact: int) -> int:
    if fact == 0:
        return 0
    if fact == 1:
        return 1
    return fact * factorial(fact - 1)
    


def reverse_string(word: str)->str:
    if len(word) == 1:
        return word[0]
    
   
    
    return  reverse_string(word[1:]) + word[0]
    
def power(base: int, exp: int)-> int:
    if exp == 0:
        return 1
    
    return base * power(base, exp -1) 

def count_up_2(num : int)-> list[int]:
    if num == 1:
        return [num]
    
    number = count_up_2(num - 1)
    number.append(num)
    return number

print(count_up_2(100))