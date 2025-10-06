def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words(filepath):
    book_text = get_book_text(filepath)
    words = book_text.split()
    return words

def get_num_letters(book_text):
    book_text = book_text.lower()
    letters = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0, " ":0, ".":0, ",":0, "!":0, "?":0, "'":0, "-":0, "\n":0}
    for letter in book_text:
        if letter in letters:
            letters[letter] += 1
    return letters

def sort_on_letters(item):
    return item["num"]

def sort_letters(letters):
    sorted_list = []
    for letters, count in letters.items():
        paar_dict = {"char": letters, "num": count}
        sorted_list.append(paar_dict)

    sorted_list.sort(key=sort_on_letters, reverse=True)
    return sorted_list