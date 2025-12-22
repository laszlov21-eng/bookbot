with open(file="books/frankenstein.txt") as f:
    file_contents = f.read()

def get_book_text(filepath):
    return  file_contents

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    char_counts= {}
    for char in text.lower():
        if char in char_counts:
           counter = char_counts[char]
           counter+= 1
        else:
           counter = 1
        char_counts[char] = counter
    return char_counts

def sort_character_counts(char_counts):
    return dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))