 # Define a function to find the frequency of each element in a list
def frequency_of_elements(input_list):
    # Create an empty dictionary to store the frequency of each element
    frequency_dict = {}
    
    # Iterate through each element in the input list
    for element in input_list:
        # If the element is already in the dictionary, increment its count
        if element in frequency_dict:
            frequency_dict[element] += 1
        # If the element is not in the dictionary, add it with a count of 1
        else:
            frequency_dict[element] = 1
            
    return frequency_dict

# Example usage
my_list = [1, 2, 2, 3, 3, 3, 4]
result = frequency_of_elements(my_list)
print(result)  # Output: {1: 1, 2: 2, 3: 3, 4: 1}
