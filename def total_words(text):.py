def get_book_text(text):
    with open(text) as f:
        text_contents = f.read()
    return text_contents


def main():
      text = get_book_text("books/frankenstein.txt")
    print(text)


main()












