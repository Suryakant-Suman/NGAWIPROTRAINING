def write_numbers_to_file(file_name):
    with open(file_name, "w") as file:
        for i in range(1, 6):
            file.write(str(i) + "\n")
