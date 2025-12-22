with open(file="books/frankenstein.txt") as f:
    file_contents = f.read()

def get_book_text(filepath):
    return  file_contents

def get_num_words(text):
    words = text.split()
    return len(words)
