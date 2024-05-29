import numpy as np
import matplotlib.pyplot as plt

def is_one_to_one(func, dom):
    set = []
    for x in dom:
        value = func(x)
        if value in set:
            return False
        set.append(value)
        print(f"f({x}) = {value}")
    return True

def InjectivePlot(func, dom):
    x = np.array(dom)
    y = np.array([func(val) for val in dom])
    plt.plot(x, y, marker = 'o', color = 'hotpink', ms = '6')  
    font1 = {'fontsize': 15}
    fon2 = {'fontsize': 20}
    plt.xlabel('x', fontdict= font1)
    plt.ylabel('f(x)', fontdict = font1)
    plt.title('One-to-One Function', fontdict = font1)
    plt.grid(axis = 'y')
    plt.savefig('One to one.png')  

def f(x):
    return x + 1

domain = [-1, -2, -3, -4, 1, 2, 3, 4]
result = is_one_to_one(f, domain)
print(f"Is the function is Injective: {result}")
InjectivePlot(f, domain)
