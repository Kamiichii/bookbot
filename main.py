def sort_on(d):
    return d["num"]

def sort_dict(num_chars_dict):
    dictionary = count_unique_letters()
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char":ch,"num":num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_unique_letters():
    with open("books/frankenstein.txt") as f:
        dictionary = {}
        text =f.read()
        text_lowered = text.lower()
        for character in text_lowered:
            if character in dictionary:
                dictionary[character] += 1
            else:
                dictionary[character] = 1
        return dictionary

def count_words():
    word_count = 0
    with open("books/frankenstein.txt") as f:
        text = f.read()
        count_of_words = len(text.split())
        return count_of_words

def print_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
def main():
    chars_sorted_list = sort_dict(count_unique_letters())
    print(f"--Report of books/frankenstein.txt-- \n {count_words()} words found in the doccument \n ")
    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times \n -- End report -- " )


main()

      
      