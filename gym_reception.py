# gym reception desk

# taking details from the user
name = input("Enter member name: ")
age = int(input("Enter member age: "))
classes = int(input("Enter classes booked: "))
fee = float(input("Enter monthly fee: "))
status = input("Is membership active? yes/no: ")

# Boolean variable
active = status.lower() == "yes"

# New class booking
new_class = input("Book new class? (yes/no): ")

# Assignment operator
if new_class.lower() == "yes":
    classes += 1

# Membership operator
name_contains_e = 'e' in name.lower()

# Identity and logical operators
eligible = (
    active is True
    and age > 15 
    and classes < 4
    )

# Display details
print("\n========== GYM MEMBERSHIP SUMMARY ==========")
print("Name", name)
print("Age", age)
print("Classes Booked", classes)
print("Monthly Fee", fee)
print("Active Membership", active)
print("Name contains e", name_contains_e)

if eligible:
    print("Membership Status: Eligible")
else:
    print("Membership Status: Not Eligible")








