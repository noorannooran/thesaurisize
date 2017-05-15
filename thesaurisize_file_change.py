from PyDictionary import PyDictionary
import random

dictionary = PyDictionary()
thesaurisized = '\n'
synonyms = list()
the_line = ''
f = open ('resources/testfile.txt', 'r+')
rows = f.readlines()

for sentence in rows:
    words = sentence.split(" ")
    for word in words:
        synonyms = dictionary.synonym(word)
        if synonyms is None:
            thesaurisized += word + " "
        else:
            max_x = len(synonyms) - 1
            i = random.randint(0, max_x)
            thesaurisized += synonyms[i] + " "

    thesaurisized += "\n"


f.write(thesaurisized)
f.close()
