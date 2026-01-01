from stats import get_num_words, get_num_chars, num_chars_to_sorted_list

def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return content

def main():
    content = get_book_text("books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(content)} total words")
    counts = get_num_chars(content)
    for c in num_chars_to_sorted_list(counts):
        print(f"{c['char']}: {c['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()