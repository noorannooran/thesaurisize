from PyDictionary import PyDictionary
import random

dictionary = PyDictionary()
word = "apple"
meaning_1 = dictionary.meaning(word)

var_type = type(meaning_1)
print(var_type)

synonym_nouns = list()
if meaning_1['Noun']:
    synonyms = dictionary.synonym(word)
    if synonyms is None:
        print("no synonyms found")
    else:
        for synonym in synonyms:
            try:
                if dictionary.meaning(synonym)['Noun']:
                    synonym_nouns.append(synonym)
                else:
                   continue
            except KeyError as e:
                print(str(e))

        if synonym_nouns is None:
            print(word)
        else:
            x_max = len(synonym_nouns) -1
            print(synonym_nouns[random.randint(0, x_max)])
            
        
      

