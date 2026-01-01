def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return content


def count_words_number(text):
    word_list = text.split()
    return len(word_list)


def main():
    text = get_book_text("books/frankenstein.txt")
    num = count_words_number(text)
    print(f"Found {num} total words")
          
if __name__ == "__main__":
    main()