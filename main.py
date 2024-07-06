def main():
    book_dir = "books/"
    book_name = "frankenstein"
    content = get_book_text(book_dir+book_name+".txt")
    word_count = get_word_count(content)
    print(content)
    print(f"This book has: {word_count} words")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(text):
    return len(text.split())

main()


