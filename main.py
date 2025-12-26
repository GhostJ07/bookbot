from stats import word_counter, char_counter, sorted_letters
import sys
import string

def get_book_text(path):
        with open(path) as f:
            return f.read()

def main ():
    if  len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:     
        book_path = sys.argv[1]
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
