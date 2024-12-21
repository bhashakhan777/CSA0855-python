 
def separate_vowels_consonants(input_string):
    vowels = "aeiouAEIOU"
    consonants = ""
    vowels_found = ""

    for char in input_string:
        if char.isalpha():  
            if char in vowels:
                vowels_found += char  
            else:
                consonants += char  

    return vowels_found, consonants

 
input_string = "Hello World"
vowels, consonants = separate_vowels_consonants(input_string)
print("Vowels:", vowels)
print("Consonants:", consonants)
