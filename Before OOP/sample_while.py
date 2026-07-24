condition=True

while condition:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))

    add=a+b
    print(f"{a}+{b} = {add}")

    print("--------------------")
    print("Do you still want to calculate? ")
    print("--------------------")

    response=input("To continue enter 'yes': ")

    if response.lower()=='yes':
        condition=True
    else:
        condition=False
