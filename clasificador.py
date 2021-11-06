# A01328928 - A01328720 - A01731843
import string
import sys
import codecs

filename = 'yelp_labelled.txt'  

def countWords(str):
    occurrences = dict()
    words = str.split()

    for word in words:
        if word in occurrences:
            occurrences[word] += 1
        else:
            occurrences[word] = 1

    return occurrences

try:
    with open(filename,'r',encoding="utf-8") as f:
        data = f.read()
    with open(filename,"w+",encoding="utf-8") as f:
        for word in data:
            out = ''.join([i for i in word if i not in string.punctuation]).lower()
            f.write(out)
    print(countWords(data))
except FileNotFoundError:
    print("File not found")
