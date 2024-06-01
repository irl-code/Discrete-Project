import numpy as np
import matplotlib.pyplot as plt
def IsBijective(func , dom, codom):
    def is_one_to_one():
        set = []
        for x in dom:
            value = func(x)
            if value in set:
                return False
            set.append(value)
            print(f"f({x}) = {value}")
        return True
    
    def is_onto():
        check = 0
        set = []
        for x in dom:
            value = func(x)
            if value in codom:
                if value not in set: 
                    set.append(value)
                    check += 1  
        if len(set) == len(codom):
            return True
        else:
            return False    
    if (is_one_to_one == True and is_onto == True):
        return True
    else:
        return False

def f(x):
    return 2 * x

Domain = [2, 4, 6, 8]
Codomain = [4, 8, 12, 16]

result = IsBijective(f , Domain, Codomain)
print(f"Is the function is Bijective: {result}")
