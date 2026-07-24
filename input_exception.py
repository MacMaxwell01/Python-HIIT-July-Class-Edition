try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a second number: "))
    c = int(input("Enter a third number: "))

    add = a + b + c
    print(f"{a} + {b} + {c} = {add}")

except ValueError:
    print("User enterd wrong input")

number = "12"
print(number.isdecimal())

