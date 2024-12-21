def length_of_last_words(s: str) ->int:
    S = s.strip()
    words = s.split('')
    return len(words[-1]) if words else 0
