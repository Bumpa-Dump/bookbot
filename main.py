def main(location):
    with open(location) as f:
        file_contents = f.read().lower()
    usable_dict = charcount(file_contents)
    usable_dict.sort(key=organize, reverse=True)
    print("--- Begin Report of ", location, " ---")
    print("Total Word Count: ", wordcount(file_contents))
    print("")
    presentation(usable_dict)

def wordcount(text):
    wordslist = text.split()
    return len(wordslist)

def charcount (text):
    char_dict = {}
    output_list = list()
    for char in text:
        if char.isalpha() == False:
            pass
        elif char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    for item in char_dict:
        output_list.append({"letter": item, "count": char_dict[item]})
    return output_list

def organize(dict):
    return dict["count"]

def presentation(ls_of_dicts):
    for item in ls_of_dicts:
        print("The ", item["letter"], " character was found ", item["count"], " times")


main("books/frankenstein.txt")