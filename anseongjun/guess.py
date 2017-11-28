class Guess:

    def __init__(self, word):
        self.guessedChars = []
        self.numTries = 0
        self.secretWord = word
        self.currentStatus = '_ ' * len(self.secretWord)
        self.secretWord = ' '.join(self.secretWord)
        self.secretWordIndex = self.secretWord.split(' ')
        self.currentStatusList = self.currentStatus.split()
        pass

    def display(self):
        print("Currnet:",self.currentStatus)
        print("Tried:",self.numTries)

        pass


    def guess(self, character):
        if character in self.guessedChars:
            pass
        else:
            self.guessedChars += character
            pass
        if self.secretWord.count(character)==0:
            self.numTries += 1

        for i in range(self.secretWord.count(character)):
            indexNumber = self.secretWordIndex.index(character)
            self.currentStatusList[indexNumber] = self.secretWordIndex[indexNumber]
            self.secretWordIndex[indexNumber] = 'null'
            self.currentStatus = ' '.join(self.currentStatusList)

            if self.secretWord == self.currentStatus:
                return True
