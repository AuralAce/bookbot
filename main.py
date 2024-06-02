def character_count(book):
    lower = book.lower()
    char_dict = {}
    for letter in lower:
        if letter not in char_dict:
            char_dict[letter] = 1
        char_dict[letter] += 1
    return char_dict

def word_count(book):
    words = book.split()
    count = 0
    for word in words:
        count += 1
    return count

def dict_to_list(dict):
    list = []
    for key, val in dict.items():
        list.append({'char': key, 'count': val})
    list.sort(reverse=True, key=sort_on)
    return list

def sort_on(dict):
    return dict["count"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    f_path = "books/frankenstein.txt"
    frankenstein = get_book_text(f_path)
    num_words = word_count(frankenstein)
    char_count = character_count(frankenstein)
    char_list = dict_to_list(char_count)
    print(f"--- Begin report of {f_path} ---")
    print(f"{num_words} found in the document")
    for dict in char_list:
        if dict['char'].isalpha():
            print(f"The '{dict['char']}' character was found {dict['count']} times")
    print("--- End report ---")
        
main()