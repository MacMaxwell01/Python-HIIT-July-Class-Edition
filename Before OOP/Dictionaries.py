# Declare an empty dictionary
student = {}

# Collect details from the user
student["First Name"] = input("Enter your first name: ")
student["Surname"] = input("Enter your surname: ")
student["Age"] = int(input("Enter your age: "))
student["Gender"] = input("Enter your gender: ")
student["Department"] = input("Enter your department: ")
student["Level"] = input("Enter your level: ")
student["Matric Number"] = input("Enter your matric number: ")

# Print the dictionary
print("\nStudent Details:")
print(student)