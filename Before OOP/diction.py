my_table = {"color":"red", "owner": "HIIT","no_of_legs":4, "is_good": True, "food":"Amala"}

print(my_table.get("color"))
print(my_table["color"])

#getting the owner

owner = my_table.get("owner")
print(f"Table Owner is: {owner}")

my_table["food"] = "Amala and Gbegiri"
my_table["color"] = "Green"
print(my_table)

print(my_table.get("food"))
