from PyDictionary import PyDictionary
import random

class Thesaurisize:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    #returns true if word is key(noun, verb, etc)
    def isKey(self, word, key):
        try:
            key = key.title()
            if self.dictionary.meaning(word)[key]:
                return True
            else:
                return False
        except KeyError as e:
            return False

    #returns true if input is a word
    def isWord(self, word):
        try:
            if self.dictionary.meaning(word) is None:
                return False
            else:
                return True
        except Exception as e:
            return False

    #returns true if word has synonyms
    def hasSynonyms(self, word):
        synonyms = self.dictionary.synonym(word)
        if synonyms is None:
            return False
        else:
            return True

    #returns a list of synonyms
    def findSynonyms(self, word):
        synonyms = self.dictionary.synonym(word)
        if synonyms is None:
            return word
        else:
            return synonyms

    #returns a list of synonyms with the same key(Noun, Verb, etc)
    def findSynonymKeys(self, word, key):
        key = key.title()
        synonym_keys = list(word)
        if self.hasSynonyms(word) is True:
            synonyms = self.findSynonyms(word)
            for word in synonyms:
                if self.isKey(word, key) is True:
                    synonym_keys.append(word)
        return synonym_keys
    
     #returns a random word from a list of words   
    def randomWord(self, word_list):
        if len(word_list) < 1:
            return word_list
        else:
            x_max = len(word_list) -1
            random_word = word_list[random.randint(0, x_max)]
            return random_word


def main():
    dictionary = PyDictionary()
    test = Thesaurisize(dictionary)
    #print("Enter a sentence")
    #sentence = input(">")
    sentence = "The apple falls far from the tree"
    words = sentence.split(" ")
    thesaurisized = ' '
    key = 'Noun'
    
    for word in words:
        if test.isWord(word) is True:
            if test.isKey(word, key) is True:
                synonyms = test.findSynonymKeys(word, key)
                thesaurisized += test.randomWord(synonyms) + " "
            else:
                thesaurisized += word + " "
        else:
            thesaurisized += word + " "

    print(thesaurisized)


if __name__ == "__main__":
    main()
    
##def random_synonym(word):
##    synonyms = dictionary.synonym(word)
##    if synonyms is None:
##        return word
##    else:
##        max_x = len(synonyms)
##        i = random.randint(0, max_x)
##        return synonyms[i]
##
##def random_synonym(line):
##    for word in line:
##        new_line += random_synonym(word) + " "
##    return new_line
##            
##def thesaurisize_line():
##    print("Enter a sentence")
##    sentence_input = input(">")
##    words = sentence_input.split(" ")
##
##    for word in sentence:
##        print(random_synonym(word) + " ") 
