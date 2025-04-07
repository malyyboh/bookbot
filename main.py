import sys
from stats import count_words, count_characters, sort_char_dict

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    num_char = count_characters(text)
    char_dict = sort_char_dict(num_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in char_dict:
        for key in dict:
            print(f"{key}: {dict[key]}")
    print("============= END ===============")


main()
