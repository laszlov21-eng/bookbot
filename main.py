import sys
from stats import get_book_text, get_num_words, get_chars_dict, sort_character_counts

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(filepath=sys.argv[1])
    char_counts=get_chars_dict(book_text)
    sorted_char_counts=sort_character_counts(char_counts)
    print_report(sys.argv[1], get_num_words(book_text), sorted_char_counts)  
    
def print_report(filepath, num_words, sorted_char_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_char_counts:
        print(f"{entry['char']}: {entry['num']}")

if __name__ == "__main__":
    main()
