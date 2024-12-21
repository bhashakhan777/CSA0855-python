
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def count_numbers():
    prime_count = 0
    composite_count = 0
    numbers = input("Enter numbers separated by spaces: ").split()
    
    for number in numbers:
        try:
            num = int(number)
            if is_prime(num):
                prime_count += 1
            elif num > 1:
                composite_count += 1
        except ValueError:
            print(f"{number} is not a valid integer. Skipping.")
    
    print(f"Total prime numbers: {prime_count}")
    print(f"Total composite numbers: {composite_count}")


count_numbers()
