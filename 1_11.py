def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            with open(destination_file, 'w') as dest:
                for line in src:
                    dest.write(line)
        print(f"\nContents are copied from {source_file} to {destination_file} Successfully.")
    except FileNotFoundError:
        print(f"\nThe file {source_file} does not exist.")
    except IOError as e:
        print(f"An error occurred: {e}")

# Take input from user:
source_file = input("\nEnter the source file name: ")
destination_file = input("\nEnter the destination file name: ")
copy_file(source_file, destination_file)  # Calling the function