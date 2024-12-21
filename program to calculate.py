# Function to calculate power
def power(x, n):
    return x ** n

# Function to add
def add(x, n):
    return x + n

# Function to subtract
def subtract(x, n):
    return x - n

# Function to multiply
def multiply(x, n):
    return x * n


def divide(x, n):
    if n != 0:
        return x / n
    else:
        return "Cannot divide by zero"


def main():
    x = float(input("Enter the value of x: "))
    n = float(input("Enter the value of n: "))
    
    print("Choose an operation:")
    print("1. Power")
    print("2. Addition")
    print("3. Subtraction")
    print("4. Multiplication")
    print("5. Division")
    
    choice = input("Enter choice (1/2/3/4/5): ")
    
    if choice == '1':
        print(f"{x} raised to the power of {n} is {power(x, n)}")
    elif choice == '2':
        print(f"The sum of {x} and {n} is {add(x, n)}")
    elif choice == '3':
        print(f"The difference when {n} is subtracted from {x} is {subtract(x, n)}")
    elif choice == '4':
        print(f"The product of {x} and {n} is {multiply(x, n)}")
    elif choice == '5':
        print(f"The result of dividing {x} by {n} is {divide(x, n)}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
