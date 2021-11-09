# A01328928 - A01328720 - A01731843
import string
import sys
import codecs
import math
import random

filename = 'yelp_labelled.txt'
outfilename = 'bayesTraining.csv'

def bayes(dictPos, dictNeg, dictTotal, pos, neg):
    dictLogs = dict()
    with open(outfilename,"w+",encoding="utf-8") as f:
        f.write("Palabra/Clase, FrecPos, FrecNeg, LogPos, LogNeg\n")
        for i, j in dictTotal.items():
            tmpPos = ((dictTotal[i][0]+1)/(pos+len(dictTotal)))
            tmpNeg = ((dictTotal[i][1]+1)/(neg+len(dictTotal)))
            instance = ("{}, {}, {}, {}\n" .format(dictTotal[i][0], dictTotal[i][1], math.log10(tmpPos), math.log10(tmpNeg)))
            dictLogs[i] = instance
            # print(instance)
            f.write("{}, {}".format(i, instance))
    return dictLogs

def bayesEvaluation(evD, res, pos, neg, total):
    instanceNumbers = evD.keys()
    resKeys = res.keys()
    posibilidadPositiva = math.log10(pos/total)
    posibilidadNegativa = math.log10(neg/total)
    with open("evaluatedSet.csv","w+",encoding="utf-8") as f:
        f.write("Instancia, LogPos, LogNeg, Clase, ClaseReal\n")
        # sentences = evD.values()
        for ins, sentence in evD.items():
            separateSent = sentence.split()
            claseReal = separateSent[len(separateSent)-1]
            separateSent.pop()
            tmpPos = posibilidadPositiva
            tmpNeg = posibilidadNegativa
            for word in separateSent:
                if word in resKeys:
                    # print(word, res[word].split(',')[2], res[word].split(',')[3])
                    tmpPos += float(res[word].split(',')[2])
                    tmpNeg += float(res[word].split(',')[3])
            if tmpPos>tmpNeg:
                f.write("{}, {}, {}, 1, {}\n" .format(ins, tmpPos, tmpNeg, claseReal))
            else:
                f.write("{}, {}, {}, 0, {}\n" .format(ins, tmpPos, tmpNeg, claseReal))
    # print(pos)
    # print(neg)

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
    evaluatingData = dict()
    sentences = str.split('\n') #separar por oraciones
    rnd = random.randrange(799)
    # print(len(sentences))
    while len(evaluatingData)<100:
        evaluatingData[rnd] = sentences[rnd]
        sentences.pop(rnd)
        rnd+=1
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
    vocabulario = {**occurrencesPos , **occurrencesNeg}
    words_table = mergeDict(occurrencesNeg, occurrencesPos)
    res = bayes(occurrencesPos, occurrencesNeg, words_table, palabrasPos, palabrasNeg)
    # print(res["not"].split(',')[2])
    # print(res["not"].split(',')[3])
    bayesEvaluation(evaluatingData, res, positivas, negativas, total)

    #PRINTS PARA DEBUGEAR
    # print("Palabras positivas: {}" .format(palabrasPos))
    # print("Palabras negativas: {}" .format(palabrasNeg))
    # print("Oraciones Positivas: {}" .format(positivas/total))
    # print("Oraciones Negativas: {}" .format(negativas/total))
    # print("Vocabulario: {}" .format(len(vocabulario)))
    # # print("Positivas: {}" .format(occurrencesPos))
    # # print("\nNegativas: {}" .format(occurrencesNeg))
    # print("")
    # print(len(words_table))

try:
    with open(filename,'r',encoding="utf-8") as f:
        trainingData = f.read()
    with open(filename,"w+",encoding="utf-8") as f:
        for word in trainingData:
            out = ''.join([i for i in word if i not in string.punctuation]).lower()
            f.write(out)
    countWords(trainingData)
except FileNotFoundError:
    print("File not found")
