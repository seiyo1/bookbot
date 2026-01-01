from stats import get_num_words

def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return content


def main():
    text = get_book_text("books/frankenstein.txt")
    num = get_num_words(text)
    print(f"Found {num} total words")
          
if __name__ == "__main__":
    main()