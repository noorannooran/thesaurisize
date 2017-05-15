from PyDictionary import PyDictionary
import random

dictionary = PyDictionary()

print("Enter a sentence")
sentence_input = input(">")
sentence = sentence_input.split(' ')
reconstructed = ''

for word in sentence:
    synonyms = dictionary.synonym(word)
    if len(synonyms) is 0:
        reconstructed += word + " "
    else:
        max_x = len(synonyms)
        i = random.randint(0, max_x-1)
        reconstructed += synonyms[i] + " "

print(reconstructed)
