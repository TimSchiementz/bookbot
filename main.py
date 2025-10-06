import sys

from stats import get_num_words, get_book_text
from stats import get_num_letters
from stats import get_book_text
from stats import sort_letters
from sys import argv

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    words = get_num_words(sys.argv[1])
    print(f"Found {len(words)} total words")
    text = get_book_text(sys.argv[1])
    letters = get_num_letters(text)
    sorted_letters = sort_letters(letters)
    for pair in sorted_letters:
        print(f"{pair["char"]}: {pair["num"]}")
main()