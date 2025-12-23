def get_book_text(filepath):
    with open(file=filepath) as f:
        file_contents = f.read()
    return  file_contents

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
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
        final_listed_counts = []
        listed_counts = list(char_counts.items())
        for key in listed_counts:
            if key[0].isalpha():
                new_dict = {"char": key[0], "num": key[1]}
                final_listed_counts.append(new_dict)
        final_listed_counts.sort(key=lambda x: x["num"], reverse=True)
        return final_listed_counts