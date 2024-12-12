import string

def main():
    book_path = "/home/gilles/workspace/github.com/GhostJ07/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    char_dict = get_character_count(text)
    special_char = []
    for char in char_dict:
        if not char.isalpha():
            special_char.append(char)
    for char in special_char:
        del char_dict[char]

    letters = []

    for letter in char_dict:
        letters.append({"letter": letter, "num": char_dict[letter]})
    
    letters.sort(reverse=True, key=sort_on)
    print(letters)
    
    print(f"--- Begin report of {book_path} ---\n")
    
    print(f"{word_count} words found in the document \n")

    for letter in letters:
        print(f"The '{letter['letter']}' character was found {letter['num']} times")
    
    print("\n--- End report --- ")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    count = {}

    for c in text:
        lowered = c.lower()
        if lowered in count:
            count[lowered] += 1
        else:
            count[lowered] = 1
    return count

def sort_on(dict):
    return dict["num"]



main ()


