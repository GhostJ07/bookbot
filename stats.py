def word_counter(text):
     wordList = text.split()
     return len(wordList)

def char_counter(text):
     count = {}
     for c in text:
        lowered = c.lower()
        if lowered in count:
            count[lowered] += 1
        else:
            count[lowered] = 1
     return count

def sorted_letters(char_dict):
    special_char = []
    for char in char_dict:
        if not char.isalpha():
            special_char.append(char)
    for char in special_char:
        del char_dict[char]

    letters = []

    for letter in char_dict:
        letters.append({"letter": letter, "num": char_dict[letter]})
    
    letters.sort(reverse=True, key=lambda dict: dict["num"])
    return letters
        
