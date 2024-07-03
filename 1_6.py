def reverse_number(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_palindrome(n):
    while not is_palindrome(n):
        reversed_n = reverse_number(n)
        n = n + reversed_n
        print(f"After adding {reversed_n}, new number is {n}")
    return n

original_number = int(input("Enter a number: "))

palindrome = find_palindrome(original_number)

print(f"The palindrome is: {palindrome}")
