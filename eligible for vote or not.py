
def check_voting_eligibility(age):
    
    voting_age = 18
    if age >= voting_age:
        return "You are eligible to vote."
    else:
        years_left = voting_age - age
        return f"You are not eligible to vote. You have {years_left} years left to be eligible."


age = int(input("Enter your age: "))
result = check_voting_eligibility(age)
print(result)
