def harmonic_sum(n: int):
    if n == 0:
        return 0;
    if n == 1:
        return 1/n
    
    number = harmonic_sum(n - 1)
    number += 1/n
    return  number


print(harmonic_sum(100))