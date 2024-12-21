
def count_factors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

n = 12
print(f"The number of factors of {n} is: {count_factors(n)}")
