
def calculate_square_and_cube(number):
    square = number ** 2  
    cube = number ** 3    
    return square, cube

decimal_number = 3.5
square, cube = calculate_square_and_cube(decimal_number)
print(f"The square of {decimal_number} is {square}")
print(f"The cube of {decimal_number} is {cube}")
