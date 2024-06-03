def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print(wordcount(file_contents))
    charcount(file_contents)

def wordcount(text):
    wordslist = text.split()
    return len(wordslist)

def charcount (text):
    char_dict = {"a" : 0}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    print(char_dict)


main()