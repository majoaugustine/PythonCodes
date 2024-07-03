def check_substring():
    main_string = input("Enter the main string: ")
    substring = input("Enter the substring to check: ")
    if substring in main_string:
        print(f"'{substring}' is a substring of '{main_string}'")
    else:
        print(f"'{substring}' is not a substring of '{main_string}'")

def count_occurrences():
    string = input("Enter the string: ")
    char = input("Enter the character to count: ")
    count = string.count(char)
    print(f"Number of occurrences of '{char}' in '{string}': {count}")

def replace_substring():
    main_string = input("Enter the main string: ")
    old_substring = input("Enter the substring to replace: ")
    new_substring = input("Enter the new substring: ")
    new_string = main_string.replace(old_substring, new_substring)
    print(f"Modified string: '{new_string}'")

def convert_to_upper():
    string = input("Enter the string to convert to uppercase: ")
    uppercase_string = string.upper()
    print(f"Uppercase string: '{uppercase_string}'")

while True:
    print("\nMenu:")
    print("1. Check if String is a Substring of Another String")
    print("2. Count Occurrences of Character")
    print("3. Replace a substring with another substring")
    print("4. Convert to Capital Letters")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        check_substring()
    elif choice == '2':
        count_occurrences()
    elif choice == '3':
        replace_substring()
    elif choice == '4':
        convert_to_upper()
    elif choice == '5':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")