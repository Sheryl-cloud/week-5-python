
# file_handling_assignment.py

def create_and_write_file():
    try:
        # Create and open the file in write mode
        with open('my_file.txt', 'w') as file:
            # Write three lines of text (mix of strings and numbers)
            file.write("Hello, this is the first line.\n")
            file.write("This is the second line, with a number: 42\n")
            file.write("Third line with another number: 100\n")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
    finally:
        print("Finished file writing operation.")

def read_file():
    try:
        # Open the file in read mode and display its contents
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("File Contents:\n")
            print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    finally:
        print("Finished reading the file.")

def append_to_file():
    try:
        # Open the file in append mode
        with open('my_file.txt', 'a') as file:
            # Append three additional lines to the file
            file.write("This is an appended fourth line.\n")
            file.write("Appending a fifth line with a number: 256\n")
            file.write("Final appended line.\n")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        print("Finished file appending operation.")

# Call the functions to perform the tasks

# 1. Create and write to file
create_and_write_file()

# 2. Read the file content
read_file()

# 3. Append to the file
append_to_file()

# 4. Read the file content again to verify append operation
read_file()
