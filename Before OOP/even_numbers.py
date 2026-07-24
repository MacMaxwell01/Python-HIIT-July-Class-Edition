# printing odd numbers from 1-100
for even in range(1, 101, 2):
    print(even)

# printing even numbers from 1-100
for even in range(0, 101, 2):
    print(even)

def print_even_numbers(stop):
    for i in range(2, stop+1, 2):
        print(i)

numbers_to_print= int(input("Enter a number and I will print the even numbers from 1 till the number: "))
print_even_numbers(numbers_to_print)