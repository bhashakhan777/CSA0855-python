def common_divisor_coount(a, b):
    count = 0
    for i in range(1, min(a, b) + 1):
        if a% i ==0 and b & i ==0:
            count +=1
            return count
        num1 = 12
        num2 = 18
        result = common_divisors_count(num1, num2)
        print(f"the number of common divisors of {num1} amd {num2} is: {result}")
