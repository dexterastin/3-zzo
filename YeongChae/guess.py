class Guess:

    def __init__(self, word):
        self.secretWord=word
        self.currentStatus=[]
        for idx in range(len(self.secretWord)):
            self.currentStatus.append("_")
        self.guessedChars = set()
        self.numTries=0


    def display(self):
        print("Current: "+ (''.join(self.currentStatus)))
        print("Tries: ", self.numTries)


    def guess(self, character):
        self.guessedChars.add(character)
        self.fIdx=0
        i=0

        while i < len(self.secretWord):
            if character==self.secretWord[i]:
                self.currentStatus[i] = self.secretWord[i]
                self.fIdx = self.fIdx + 1
            i=i+1

        if self.fIdx==0:
            self.numTries=self.numTries+1

        if ''.join(self.currentStatus)==self.secretWord:
            return True

        else:
            return False



