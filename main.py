import sys
from stats import get_book_text, get_char_num, get_num_words, sort_dict_list

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    char_dict = get_char_num(text)
    print_report(filepath, num_words, char_dict)

def print_report(filepath, word_count, char_dict):
    sorted_list = sort_dict_list(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in sorted_list:
        print(f"{d['char']}: {d['num']}")
    print("============= END ===============")

main()
