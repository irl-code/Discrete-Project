import numpy as np
import matplotlib.pyplot as plt
def is_onto(func, dom, codom):
    check = 0
    set = []
    for x in dom:
        value = func(x)
        if value in codom:
            if value not in set: 
                set.append(value)
                check += 1  
            print(f"f({x}) = {value}")
        else:    
            print(f"f({x}) = {value} (But it is not in the codomain)")
    if len(set) == len(codom):
          print(len(set), len(codom))
          return True
    else:
        return False    

def f(x):
    return (x**2) + 10
codoMain = [11, 14, 19, 26]
doMain = [-1, 1, 2, -2, 3, 4, 7, 8, 9, 10]
result = is_onto(f, doMain, codoMain)
print(f"The function is onto: {result}")