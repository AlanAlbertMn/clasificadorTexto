# A01328928 - A01328720 - A01731843
import string
import sys
import codecs

filename = 'yelp_labelled.txt'  

def countWords(str):
    occurrencesPos = dict()
    occurrencesNeg = dict()
    sentences = str.split('\n')

    for sentence in sentences:
        if sentence.endswith("1"):
            words = sentence.split()
            for word in words:
                if word in occurrencesPos:
                    occurrencesPos[word] += 1
                else:
                    occurrencesPos[word] = 1
        else:
            words = sentence.split()
            for word in words:
                if word in occurrencesNeg:
                    occurrencesNeg[word] += 1
                else:
                    occurrencesNeg[word] = 1
    occurrencesPos.pop('1')
    occurrencesNeg.pop('0')
    print("Positivas: {}" .format(occurrencesPos))
    print("\n")
    print("Negativas: {}" .format(occurrencesNeg))

try:
    with open(filename,'r',encoding="utf-8") as f:
        data = f.read()
    with open(filename,"w+",encoding="utf-8") as f:
        for word in data:
            out = ''.join([i for i in word if i not in string.punctuation]).lower()
            f.write(out)
    countWords(data)
except FileNotFoundError:
    print("File not found")

