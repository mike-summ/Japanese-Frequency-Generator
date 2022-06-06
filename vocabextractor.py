import fugashi
from collections import Counter

def extractVocab(filePath):
        tagger = fugashi.Tagger()
        f = open(filePath, encoding="utf-8")
        text = f.read()
        test_list = []
        res = []
        output = []

        outputText = '['

        for word in tagger(text):
                test_list.append(word.feature.lemma)

        # Sorts array by frequency
        res = Counter(test_list)
        sorted_res = sorted(res, key=res.get, reverse=True)

        for i in sorted_res:
                if i not in output:
                        output.append(i)

        # Places the output into a String variable
        freq  = 0
        for value in output:
                outputText += '["' + str(value) + '" ,"freq",' + str(freq) + '],\n'
                freq = freq + 1
        
        
        outputText = outputText[:-2] + ']'
        
        return outputText
