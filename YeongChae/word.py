import random

class Word:

    def __init__(self, filename, maxLength):

        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()
            if len(word) <= maxLength:
                self.words.append(word)
                self.count += 1

        print('%d words in DB' % self.count)


    def test(self):
        return 'default'


    def randFromDB(self):

        r = random.randrange(self.count)
        return self.words[r]
