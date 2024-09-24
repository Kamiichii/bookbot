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
        print(dictionary)

def count_words():
    word_count = 0
    with open("books/frankenstein.txt") as f:
        text = f.read()
        count_of_words = len(text.split())
        print(count_of_words)

def print_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
def main():
    count_unique_letters()

main()

      
      