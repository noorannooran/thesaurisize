from PyDictionary import PyDictionary
import random

dictionary = PyDictionary()
thesaurisized = ''
the_line = ''
f = open ('resources/testfile.txt', 'r')
rows = f.readlines()

for sentence in rows:
    words = sentence.split(" ")
    for word in words:
        synonyms = dictionary.synonym(word)
        if len(synonyms) is 0:
            thesaurisized += word + " "
        else:
            max_x = len(synonyms) - 1
            i = random.randint(0, max_x)
            thesaurisized += synonyms[i] + " "

    thesaurisized += "\n"


print(thesaurisized)

