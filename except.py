file_name = "file/wrong_name.txt"

try:

    with open(file_name, "r") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("File Not Found")

#This only catches file not found error only

except ZeroDivisionError:
    print("You can't divide by zero")

