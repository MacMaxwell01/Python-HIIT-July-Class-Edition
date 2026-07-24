every_body_in_class = ["Neymar", "Ronaldo","Suarez", "Mbappe", "Haaland"]
print(every_body_in_class)


first_person = every_body_in_class[0]
print(first_person)
 
last_person = every_body_in_class[-1]
print(last_person)

second_to_last_person = every_body_in_class[-2]
print(second_to_last_person)

second_to_last_person = every_body_in_class[-4]
print(second_to_last_person)

numbers = [3, 5, 7, 8, 1, 4, 6, 8, 10, 2]
numbers.sort()
print(numbers)

names = ["Zaria", "Yakubu", "Tinubu","Mohammed", "Dorcas", "Abubakar", "Balewa"]
names.sort()
print(names)

names = [
    "Zaria", 
    "Yakubu", 
    "Tinubu",
    "Mohammed", 
    "Dorcas", 
    "abubakar", 
    "balewa"
    ]
print(names)



# Adding to the list
names.append("Favour")
names.append("Ade")

# Checking the length of a list
length_of_names = len(names)
print(f"We now have {length_of_names} in this list")

print(names)

#Reoving from the list
names.remove("balewa")
print(names)

cars = ["Toyota", "BMW", "Tesla", "Mercedes", "Cybertruck"]
print(cars)
cars.insert(1,"GLE")
print(cars)
cars.pop(2)
print(cars)

names = [
    "Zaria", "Yakubu", "Tinubi", "Mohammed"]

print(names)

#Replce name
names[2]="Tinubu"
print(names)


# To merge the lists together
every_body_in_class.extend(cars)
print(every_body_in_class)