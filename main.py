def main(location):
    with open(location) as f:
        file_contents = f.read()
    usable_dict = charcount(file_contents)
    print("--- Begin Report of ", location, " ---")
    print("Total Word Count: ", wordcount(file_contents))
    print("")
    for entry in usable_dict:
        print("The '", entry, "' character appeared ", usable_dict[entry], " times.")

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
    return(char_dict)


main("books/frankenstein.txt")

# need to convert dictionary to list of dictionaries (list.append (temp_dict establish values?)), remove non-alphabetic characters (boring), and organize by frequency