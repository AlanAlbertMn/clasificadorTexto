# A01328928 - A01328720 - A01731843
import string
import sys
import codecs

filename = 'yelp_labelled.txt'  

def mergeDict(dict1, dict2):
    # Merge dictionaries and keep values of common keys in list
    dict3 = {**dict1, **dict2}
    for key, value in dict3.items():
       if key in dict1 and key in dict2:
               dict3[key] = [value[0] , dict1[key][1]]
    return dict3
    # Merge dictionaries and add values of common keys in a list
    dict3 = mergeDict(dict1, dict2)
    print('Dictionary 3 :')
    print(dict3)

def countWords(str):
    occurrencesPos = dict()
    occurrencesNeg = dict()
    sentences = str.split('\n')

    for sentence in sentences:
        if sentence.endswith("1"):
            words = sentence.split()
            for word in words:
                if word in occurrencesPos:
                    tmp = occurrencesPos[word]
                    tmp[0]+=1
                    occurrencesPos[word] = tmp
                else:
                    occurrencesPos[word] = [1, 0]
        else:
            words = sentence.split()
            for word in words:
                if word in occurrencesNeg:
                    tmp = occurrencesNeg[word]
                    tmp[1]+=1
                else:
                    occurrencesNeg[word] = [0, 1]
    positivas = occurrencesPos.get('1')[0]
    negativas = occurrencesNeg.get('0')[1]
    occurrencesPos.pop('1')
    occurrencesNeg.pop('0')
    # print("Palabras positivas: {}" .format(sum(occurrencesPos.values())))
    # print("Palabras negativas: {}" .format(sum(occurrencesNeg.values())))
    print("Oraciones Positivas: {}" .format(positivas))
    print("Oraciones Negativas: {}" .format(negativas))
    vocabulario = {**occurrencesPos , **occurrencesNeg}
    print("Vocabulario: {}" .format(len(vocabulario)))

    print("Positivas: {}" .format(occurrencesPos))
    print("\nNegativas: {}" .format(occurrencesNeg))

    words_table = mergeDict(occurrencesNeg, occurrencesPos)
    print("")
    print(words_table)


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

