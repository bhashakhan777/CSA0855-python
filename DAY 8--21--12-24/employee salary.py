 
def calculate_bonus(salary, grade):
    
    bonus = 0
    
     
    if grade == 'A':
        bonus = salary * 0.05   
    elif grade == 'B':
        bonus = salary * 0.10  
    
     
    if salary < 10000:
        bonus += salary * 0.02   
    
     
    total_salary = salary + bonus
    return total_salary, bonus

 
salary = float(input("Enter the salary of the employee: "))
grade = input("Enter the grade of the employee (A/B): ").upper()

 
total_salary, bonus = calculate_bonus(salary, grade)

 
print(f"The bonus for the employee is: ${bonus:.2f}")
print(f"The total salary after bonus is: ${total_salary:.2f}")
