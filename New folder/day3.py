# Program to check age category

age = int(input("Enter your age: "))

if 0 <= age <= 5:
    print("Category: Kids")
elif 6 <= age <= 11:
    print("Category: Child")
elif 12 <= age <= 19:
    print("Category: Teenagers")
else:
    print("Category: Adults")