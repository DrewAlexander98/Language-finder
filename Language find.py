import os.path
import string
import codecs

def main():
    print(string.printable)
    text = open_file("English.txt")
    letters = language_find(text)
    letter_sort(letters)

def open_file(filename):
    if os.path.isfile(filename):
        string = ""
        with open(filename, encoding='utf-8') as infile:
            for line in infile:
                line = line.encode('ascii',errors='ignore')
                print(str(line))
                string += str(line)
        return string
    else:
        print("Cannot locate file {0}".format(filename))
        return None

def language_find(string):
    print(string)
    string = string.replace(" ", "").replace(",", "").replace(".", "").replace(":", "").replace(";", "").replace("-", "").replace("\n", "").lower()
    dict1 = {}
    for i in range(len(string)):
        if string[i] in dict1:
            dict1[string[i]] += 1
        else:
            dict1[string[i]] = 1
    print(dict1)
    return dict1

def letter_sort(dict):
    sorted_list = []
    while len(dict) > 0:
        max = list(dict.keys())[0]
        for i in dict:
            if dict[i] > dict[max]:
                max = i
        sorted_list.append(max)
        del dict[max]
    print(sorted_list)
    return sorted_list


main()
