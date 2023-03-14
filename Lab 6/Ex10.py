def convertbase(a, base1, base2):
    n = 0
    for digit in a:
        n = n * base1 + digit
    
    result = []
    while n > 0:
        digit = n % base2
        result.append(digit)
        n //= base2
    
    return result[::-1]
  
print(convertbase([1,1,1],10,16))