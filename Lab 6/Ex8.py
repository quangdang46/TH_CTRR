def decToBinConversion(no, precision): 
    binary = ""  
    IntegralPart = int(no)  
    fractionalPart = no- IntegralPart
    while (IntegralPart):
        re = IntegralPart % 2 
        binary += str(re)  
        IntegralPart //= 2
    binary = binary[ : : -1]    
    binary += '.'
    while (precision):
        fractionalPart *= 2
        bit = int(fractionalPart)
        if (bit == 1) :   
            fractionalPart -= bit  
            binary += '1'
        else : 
            binary += '0'
        precision -= 1
    return binary  

print("Binary Equivalent:",decToBinConversion(5.5,2))


