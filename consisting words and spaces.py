def length_of_last_word(s: str) -> int:
     
    s = s.rstrip()
    
    words = s.split(' ')
     
    return len(words[-1]) if words else 0