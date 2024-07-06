def main():
    book_dir = "books/"
    book_name = "frankenstein"
    content = get_book_text(book_dir+book_name+".txt")
    word_count = get_word_count(content)
    count_dict = count_chars(content)

    print(f"This book has: {word_count} words")
    print("")
    print_chars(dict_to_list(count_dict))
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(text):
    return len(text.split())

def count_chars(text):
    count = {}
    for char in text.lower():
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    return count

def dict_to_list(d):
    new_list = []
    for key, value in d.items():
        new_list.append({'char':key, 'count':value})
    return new_list
        
def sort_on(dict):
    return dict["count"]

def print_chars(lst):
    lst.sort(reverse=True, key=sort_on)
    for item in lst:
        if item["char"].isalpha():
            print(f"The {item["char"]} character was found {item["count"]} times")

main()


