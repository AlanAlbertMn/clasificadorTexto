# A01328928 - A01328720 - A01731843
import string
import sys
import codecs
import math

filename = 'yelp_labelled.txt'

def bayes(dictPos, dictNeg, dictTotal, pos, neg):
    dictLogs = dict()
    for i, j in dictTotal.items():
        tmpPos = ((dictTotal[i][0]+1)/(pos+len(dictTotal)))
        tmpNeg = ((dictTotal[i][1]+1)/(neg+len(dictTotal)))
        print("{} {} {} {} {}" .format(i, dictTotal[i][0], dictTotal[i][1], math.log10(tmpPos), math.log10(tmpNeg)))

def mergeDict(dict1, dict2):
    # Merge dictionaries and keep values of common keys in list
    dict3 = {**dict1, **dict2}
    for key, value in dict3.items():
       if key in dict1 and key in dict2:
               dict3[key] = [value[0] , dict1[key][1]]
    return dict3

def countWords(str):
    occurrencesPos = dict()
    occurrencesNeg = dict()
    sentences = str.split('\n') #separar por oraciones
    palabrasPos = 0
    palabrasNeg = 0
    for sentence in sentences:
        if sentence.endswith("1"): #si la oracion antes de separarla termina con 1 significa que es positiva
            words = sentence.split()
            for word in words:
                palabrasPos+=1
                if word in occurrencesPos:
                    tmp = occurrencesPos[word]
                    tmp[0]+=1
                    occurrencesPos[word] = tmp
                else:
                    occurrencesPos[word] = [1, 0]
        else: #si la oracion antes de separarla termina con 0 significa que es negativa
            words = sentence.split()
            for word in words:
                palabrasNeg+=1
                if word in occurrencesNeg:
                    tmp = occurrencesNeg[word]
                    tmp[1]+=1
                else:
                    occurrencesNeg[word] = [0, 1]
    positivas = occurrencesPos.get('1')[0]
    negativas = occurrencesNeg.get('0')[1]
    palabrasPos-=positivas
    palabrasNeg-=negativas
    total = positivas + negativas
    occurrencesPos.pop('1')
    occurrencesNeg.pop('0')
    # print("Palabras positivas: {}" .format(palabrasPos))
    # print("Palabras negativas: {}" .format(palabrasNeg))
    # print("Oraciones Positivas: {}" .format(positivas/total))
    # print("Oraciones Negativas: {}" .format(negativas/total))
    vocabulario = {**occurrencesPos , **occurrencesNeg}
    # print("Vocabulario: {}" .format(len(vocabulario)))

    # # print("Positivas: {}" .format(occurrencesPos))
    # # print("\nNegativas: {}" .format(occurrencesNeg))

    words_table = mergeDict(occurrencesNeg, occurrencesPos)
    # print("")
    # print(len(words_table))
    bayes(occurrencesPos, occurrencesNeg, words_table, palabrasPos, palabrasNeg)

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

