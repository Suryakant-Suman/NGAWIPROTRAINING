from number_package.writer import write_numbers_to_file
def read_file_safely(file_name):
    try:
        with open(file_name, "r") as file:
            print("File Contents\n")
            print(file.read())
    except FileNotFoundError:
        print("File Not Found")
    except PermissionError:
        print("Permission Denied")
    except Exception as e:
        print("unexpected error", e)

if __name__ == "__main__":
    read_file_safely("f1.txt")

#writer.py

def write_file_safely(file_name):
    try:
        with open(file_name, "a") as file:
            for i in range(1, 101):
                file.write(str(i) + "\n")
            print("Number Written Successfully")

    except FileNotFoundError:
        print("File Not Found")
    except PermissionError:
        print("Permission Denied")
    except Exception as e:
        print("unexpected error", e)

if __name__ == "__main__":
    write_file_safely("f1.txt")



