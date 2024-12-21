
    # Function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case: n * factorial of (n-1)

# Example usage
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")

