from stats import get_num_words, get_book_text,get_num_characters,sort_character_counts

def main():
    print(f"Found {get_num_words(get_book_text('books/frankenstein.txt'))} total words")
    char_counts=get_num_characters(get_book_text('books/frankenstein.txt'))
    sorted_char_counts=sort_character_counts(char_counts)
    print(sorted_char_counts)
if __name__ == "__main__":
    main()
