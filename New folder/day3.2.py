2

age = int(input("Enter your age: "))

if 0 <= age <= 5:
    print("You are a Kid.")
elif 6 <= age <= 11:
    print("You are a Child.")
elif 12 <= age <= 19:
    print("You are a Teenager.")
elif age >= 20:
    print("You are an Adult.")
else:
    print("Invalid age entered.")