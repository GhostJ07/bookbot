from stats import word_counter, char_counter, sorted_letters
import string

def get_book_text(path):
        with open(path) as f:
            return f.read()

def main ():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordCount = word_counter(text)
    charCount = char_counter(text)

    print(f"============ BOOKBOT ============\n")
    
    print(f"Analyzing book found at {book_path}...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {wordCount} total words")
    print("--------- Character Count -------\n")
    for letter in sorted_letters(charCount):
        print(f"{letter['letter']}: {letter['num']}")
    
    print("\n============= END ===============\n")
    
main()
