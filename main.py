def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print()
    print(f"{num_words} words found in the document")
    print()
    print("Distribution of letters:")
    for item in get_sorted_chars_list(chars_dict):
        print(f"{item[1]} of {item[0]}'s")
    print()
    print("--- End report ---")
    get_sorted_chars_list(chars_dict)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_sorted_chars_list(chars_dict):
    list = chars_dict.items()
    chars_list = []
    for item in sorted(list, key=lambda a: a[1], reverse=True):
        if item[0].isalpha():
            chars_list.append(item)
    return chars_list


main()
