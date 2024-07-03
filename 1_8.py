def factorial_with_cache(n, cache={}):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        result = 1
    else:
        result = n * factorial_with_cache(n - 1, cache)
    cache[n] = result
    print(f"Calculated factorial of {n}: {result}")
    return result

number = int(input("Enter a number to calculate its factorial: "))
factorial = factorial_with_cache(number)
print(f"The factorial of {number} is: {factorial}")
