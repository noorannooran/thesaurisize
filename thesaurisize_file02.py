from thesaurisize import random_synonym

f = open ('resources/testfile.txt', 'r')
rows = f.readlines()

for sentence in rows:
    thesaurisized += random_synonym(sentence)
    thesaurisized += "\n"


print(thesaurisized)

