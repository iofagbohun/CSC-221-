# Imports regular expressions
import re

# This function takes a line of text and returns
# a list of words in the line


def split_line(line):
    split = re.findall('[A-Za-z]+(?:\'\"[A-Za-z]+)?', line)
    return split


# Opens the dictionary text file and adds each line to an array, then closes the file
dictionary = open("dictionary.txt")
dictionary_list = []
for item in dictionary:
    dictionary_list.append(split_line(item))
print(dictionary_list)
dictionary.close()

print("---Linear Search---")

# Opens the text for the first chapter of Alice in Wonderland
chapter_1 = open("AliceInWonderland200.txt")

# Breaks down the text by line
for each_line in chapter_1:
    # Breaks down each line to a single word
    word_list = split_line(each_line)
    # Checks each word against the dictionary array
    for each_word in word_list:
        current_word_list = 0

