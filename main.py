def count_words():
    word_count = 0
    with open("books/frankenstein.txt") as f:
        text = f.read()
        count_of_words = len(text.split())
        print(count_of_words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

count_words()

      
      