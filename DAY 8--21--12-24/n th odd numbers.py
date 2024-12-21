 
def nth_odd_after_n(n):
    
    nth_odd = 2 * n - 1
    
    next_odd = nth_odd + 2
    return next_odd


n = 5
result = nth_odd_after_n(n)
print(f"The odd number after the {n}th odd number is: {result}")
