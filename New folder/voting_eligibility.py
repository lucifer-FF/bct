# Program to check if a person is eligible for casting vote

def check_voting_eligibility(age):
    """
    Check if a person is eligible to vote based on age.
    Eligible if age >= 18 years
    """
    if age >= 18:
        return True
    else:
        return False

# Main function
if __name__ == "__main__":
    # Take age input from user
    age = int(input("Enter your age: "))
    
    # Check eligibility
    if check_voting_eligibility(age):
        print(f"Age {age}: You are ELIGIBLE to cast vote!")
    else:
        print(f"Age {age}: You are NOT ELIGIBLE to cast vote yet.")
        print(f"You need to be at least 18 years old.")
