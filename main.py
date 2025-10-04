from stats import *
import sys

# Function to read the book text from a file
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]

    # Print the book analysis report
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    book_text = get_book_text(filepath)
    print("----------- Word Count ----------")
    word_count = count_words(book_text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_count = count_characters(book_text)
    report = sorted_list(character_count)
    for char, count in report:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()