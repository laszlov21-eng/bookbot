from stats import get_num_words, get_book_text

def main():
    print(f"Found {get_num_words(get_book_text('books/frankenstein.txt'))} total words")

if __name__ == "__main__":
    main()