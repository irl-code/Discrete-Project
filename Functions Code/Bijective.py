import numpy as np
import matplotlib.pyplot as plt


def IsBijective(func, dom, codom):
    def is_one_to_one():
        set = []
        print("Checking one-to-one property")
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
        print("Checking onto property")
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

    if is_one_to_one() and is_onto():
        return True
    else:
        return False


def BijectivePlot(func, dom, codom):
    x = np.array(dom)
    y = np.array([func(val) for val in dom])
    plt.plot(x, y, marker="o", color="orange", ms="10", linewidth=3)
    font1 = {"fontsize": 15}
    font2 = {"fontsize": 20}
    plt.xlabel("x", fontdict=font1)
    plt.ylabel("f(x)", fontdict=font1)
    plt.title("Bjiective Function", fontdict=font2)
    plt.grid(axis="y")
    plt.savefig("Bijective.png")


def f(x):
    return 2 * x


Domain = [2, 4, 6, 8, 9]
Codomain = [4, 8, 12, 16]
result = IsBijective(f, Domain, Codomain)
BijectivePlot(f, Domain, Codomain)
print(f"Is the function is Bijective: {result}")
