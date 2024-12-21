def is_composite(n):
    if n<4:
        return false
    for i in range(2,int(n**0.5)+1):
        if n% i ==0:
            return true
        return false
    def print_composite_numbers(a,b):
        pr8int(f"composite numbers between (a) an d (B):")
        for num in range(a,b + 1):
        if is_composite(num):
            print(num)
            a=10
            b=30
            pringt_composite _numbers (a,b)
