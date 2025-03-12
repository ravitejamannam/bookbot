import sys
from stats import get_num_words, count_characters, sort_char_counts
def get_book_text(filepath):
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found. Please check the file path.")
        sys.exit(1)



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]  
    text = get_book_text(book_path)
    
    if text:  
        num_words = get_num_words(text)
        print(f"Found {num_words} total words")
    
        char_counts = count_characters(text)
        sorted_chars = sort_char_counts(char_counts)
        print("\nCharacter Frequency Report:")
        for item in sorted_chars:
            print(f"{item['char']}: {item['count']}")


if __name__ == "__main__":
    test_path = "books/frankenstein.txt" 
    test_text = get_book_text(test_path)


    main()