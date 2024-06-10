import numpy as np
import matplotlib.pyplot as plt


def is_onto(func, dom, codom):
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
        return True
    else:
        return False


def SurjectivePlot(func, dom):
    x = np.array(dom)
    y = np.array([func(val) for val in dom])
    plt.plot(x, y, marker="o", color="purple", ms="10", linewidth=2.8)
    font1 = {"fontsize": 15}
    font2 = {"fontsize": 20}
    plt.xlabel("x", fontdict=font1)
    plt.ylabel("f(x)", fontdict=font1)
    plt.title("Onto Function", fontdict=font2)
    plt.grid(axis="y")
    plt.savefig("Surjective.png")


def f(x):
    return x + 10


codoMain = [11, 12, 13, 14]
doMain = [1, 2, 3, 4]
result = is_onto(f, doMain)
print(f"Is the function is Surjective: {result}")
SurjectivePlot(f, doMain, codoMain)
