import os

def create_directory(directory):
    try:
        os.makedirs(directory)
        print(f"Directory '{directory}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

def list_directory(directory):
    try:
        files = os.listdir(directory)
        print(f"Listing contents of '{directory}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Directory '{directory}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def search_python_files(directory):
    try:
        py_files = [f for f in os.listdir(directory) if f.endswith('.py')]
        if py_files:
            print(f"'.py' files in '{directory}':")
            for file in py_files:
                print(file)
        else:
            print(f"No '.py' files found in '{directory}'.")
    except FileNotFoundError:
        print(f"Directory '{directory}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def remove_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' removed successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

while True:
    print("\nOptions:")
    print("1. Create a directory")
    print("2. List directory contents")
    print("3. Search for '.py' files")
    print("4. Remove a particular file")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        directory = input("\nEnter the directory name to create: ")
        create_directory(directory)
    elif choice == '2':
        directory = input("\nEnter the directory name to list: ")
        list_directory(directory)
    elif choice == '3':
        directory = input("\nEnter the directory name to search for '.py' files: ")
        search_python_files(directory)
    elif choice == '4':
        file_path = input("\nEnter the file path to remove: ")
        remove_file(file_path)
    elif choice == '5':
        print("\nExiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")