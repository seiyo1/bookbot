def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return content


def main():
    ret = get_book_text("books/frankenstein.txt")
    print(ret)
    
if __name__ == "__main__":
    main()