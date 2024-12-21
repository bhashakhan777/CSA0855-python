
def arrange_letters_reverse(word):
    
    letters = list(word)

    letters.sort(reverse=True)

    return ''.join(letters)


result = arrange_letters_reverse("example")
print(result)  
