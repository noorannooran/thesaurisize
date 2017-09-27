from PyDictionary import PyDictionary
import random

dictionary = PyDictionary()
thesaurisized = ''

#open and read file
f = open('resources/testfile2.txt', 'r+')
rows = f.readlines()

#empty list to hold noun synonyms
synonym_nouns = list()

def isNoun(word):
    meaning = dictionary.meaning(word)
    if meaning is None:
        return false
    else:
        if meaning[

#iterate through lines of file
for sentence in rows:
    words = sentence.split(" ")
    for word in words:
        if dictionary.meaning(word) is None:
            continue
        #if the key is a noun, use thesaurisize
        else:
            meaning = dictionary.meaning(word)
            try:
                if meaning['Noun']:
                    synonyms = dictionary.synonym(word)
                    if synonyms is None:
                        thesaurisized += word + " "
                    else:
                        for synonym in synonyms:
                            try:
                                if dictionary.meaning(synonym) is None:
                                    continue
                                elif dictionary.meaning(synonym)['Noun']:
                                    synonym_nouns.append(synonym)
                                else:
                                    continue
                            except KeyError as e:
                                print(str(e))
                        if synonym_nouns is None:
                            thesaurisized += word + " "
                        else:
                            max_x = len(synonym_nouns) -1
                            i = random.randint(0, max_x)
                            thesaurisized += synonym_nouns[i] + " "
                            break
            except KeyError as e:
                continue
            thesaurisized += "\n"

print(thesaurisized)

