# Discrete Mathematics Function Checker

## Overview

This project contains a Python script to determine whether a given function is injective (one-to-one), surjective (onto), or bijective (both one-to-one and onto). The script evaluates these properties based on a specified domain and codomain.

## Functions Explained

### Injective (One-to-One)

A function \( f: A \rightarrow B \) is injective if every element of the domain \( A \) maps to a unique element in the codomain \( B \). In other words, no two different elements in \( A \) map to the same element in \( B \).

### Surjective (Onto)

A function \( f: A \rightarrow B \) is surjective if every element of the codomain \( B \) has at least one pre-image in the domain \( A \). In other words, the function covers the entire codomain.

### Bijective

A function \( f: A \rightarrow B \) is bijective if it is both injective and surjective. This means every element in \( A \) maps to a unique element in \( B \) and every element in \( B \) is covered.

## Code Description

The code provides a function `IsInjective`, `IsSurjective`, `IsBijective` to check whether a given function is bijective by evaluating its injective and surjective properties. Here's how the code works:

### Functions and Methods

- **IsBijective(func, dom, codom)**
  - This is the main function that checks if the given function `func` is bijective.
  - It contains two helper functions:
    - **is_one_to_one()**: Checks if `func` is injective by ensuring no two elements in `dom` map to the same element in `codom`.
    - **is_onto()**: Checks if `func` is surjective by ensuring every element in `codom` is mapped by some element in `dom`.
  - If both conditions are met, `IsBijective` returns `True`, indicating the function is bijective.

### Example Function

- **f(x)**
  - This is a sample function defined as \( f(x) = 2x \).
  - The domain and codomain for this example are `[2, 4, 6, 8]` and `[4, 8, 12, 16]`, respectively.

### Usage

To check if the function \( f(x) = 2x \) is bijective for the given domain and codomain, run the following code:

```python
import numpy as np
import matplotlib.pyplot as plt

def IsBijective(func, dom, codom):
    def is_one_to_one():
        values_seen = []
        for x in dom:
            value = func(x)
            if value in values_seen:
                return False
            values_seen.append(value)
            print(f"f({x}) = {value}")
        return True
    
    def is_onto():
        values_seen = set()
        for x in dom:
            value = func(x)
            if value in codom:
                values_seen.add(value)
                print(f"f({x}) = {value}")
            else:
                print(f"f({x}) = {value} (But it is not in the codomain)")
        return len(values_seen) == len(codom)
    
    if is_one_to_one() and is_onto():
        return True
    else:
        return False

def f(x):
    return 2 * x

Domain = [2, 4, 6, 8]
Codomain = [4, 8, 12, 16]

result = IsBijective(f, Domain, Codomain)
print(f"Is the function bijective: {result}")
