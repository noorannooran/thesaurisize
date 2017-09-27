from PyDictionary import PyDictionary
import random

class TestNoun:
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
            print(str(e))
            return False
        
    #returns true if word is a noun
    def isNoun(self, word):
        try:
            if self.dictionary.meaning(word)['Noun']:
                return True
            else:
                return False
        except KeyError as e:
            print(str(e))
            return False

    #returns true if input is a word
    def isWord(self, word):
        try:
            if self.dictionary.meaning(word):
                return True
            else:
                return False
        except Exception as e:
            print(str(e))
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

    #returns a list of synonyms that are also nouns
    def findSynonymNouns(self, word):
        synonym_nouns = list()
        if self.hasSynonyms(word) is True:
            synonyms = self.findSynonyms(word)
            for word in synonyms:
                if self.isNoun(word) is True:
                    synonym_nouns.append(word)
        return synonym_nouns

    #returns a list of synonyms with the same key(Noun, Verb, etc)
    def findSynonymKeys(self, word, key):
        key = key.title()
        synonym_keys = list()
        if self.hasSynonyms(word) is True:
            synonyms = self.findSynonyms(word)
            for word in synonyms:
                if self.isKey(word, key) is True:
                    synonym_keys.append(word)
        return synonym_keys
    
     #returns a random word from a list of words   
    def randomWord(self, word_list):
        x_max = len(word_list) -1
        random_word = word_list[random.randint(0, x_max)]
        return random_word



def main():
    dictionary = PyDictionary()
    word = "apple"
    test = TestNoun(dictionary)
    if test.isWord(word) is True:
            synonyms = test.findSynonymNouns(word)
            print(test.randomWord(synonyms))

    word = "run"
    if test.isWord(word) is True:
            synonyms = test.findSynonymKeys(word, "Verb")
            print(test.randomWord(synonyms))
        
        

if __name__ == "__main__":
    main()
    
##dictionary = PyDictionary()
##word = "apple"
##meaning_1 = dictionary.meaning(word)
##
##var_type = type(meaning_1)
##print(var_type)
###empty list to hold synonyms that are also nouns
##synonym_nouns = list()
###if word definition contains Noun key find synonyms
##if meaning_1['Noun']:
##    synonyms = dictionary.synonym(word)
##    if synonyms is None:
##        print("no synonyms found")
##    #iterate through synonyms, if synonym is a noun add it to the list
##    else:
##        for synonym in synonyms:
##            try:
##                if dictionary.meaning(synonym)['Noun']:
##                    synonym_nouns.append(synonym)
##                else:
##                   continue
##            except KeyError as e:
##                print(str(e))
##
##        if synonym_nouns is None:
##            print(word)
##        else:
##            #choose and print random synonym noun
##            x_max = len(synonym_nouns) -1
##            print(synonym_nouns[random.randint(0, x_max)])
##            
##
