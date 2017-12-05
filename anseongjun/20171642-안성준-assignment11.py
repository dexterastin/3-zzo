import unittest

from guess import Guess
from hangman import Hangman
from word import Word

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')
        self.g1s = Hangman()
        self.g1w = Word('words.txt')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('b')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')
        #self.assertEqual(self.g2.displayCurrent(), '_ _ _ e ')
        #self.g2.guess('c')
        #self.assertEqual(self.g2.displayCurrent(), 'c _ _ e ')
        #self.g2.guess('b')
        #self.assertEqual(self.g2.displayCurrent(), 'c _ _ e ')
        #self.g2.guess('a')
        #self.assertEqual(self.g2.displayCurrent(), 'c a _ e ')
        #self.g2.guess('s')
        #self.assertEqual(self.g2.displayCurrent(), 'c a s e ')




    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('b')
        self.assertEqual(self.g1.displayGuessed(), ' b e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a b e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a b e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a b e n t u ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayGuessed(), ' a b d e n t u ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayGuessed(), ' a b d e f n t u ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayGuessed(), ' a b d e f l n t u ')
        #self.assertEqual(self.g2.displayGuessed(), ' e n ')
        #self.g2.guess('c')
        #self.assertEqual(self.g2.displayGuessed(), ' c e n ')
        #self.g2.guess('b')
        #self.assertEqual(self.g2.displayGuessed(), ' b c e n ')
        #self.g2.guess('a')
        #self.assertEqual(self.g2.displayGuessed(), ' a b c e n ')
        #self.g2.guess('s')
        #self.assertEqual(self.g2.displayGuessed(), ' a b c e n s ')

    def testHangman(self):
        self.assertEqual(self.g1s.remainingLives, 6)
        self.g1s.decreaseLife()
        self.assertEqual(self.g1s.remainingLives, 5)
        self.g1s.decreaseLife()
        self.assertEqual(self.g1s.remainingLives, 4)
        self.g1s.decreaseLife()
        self.assertEqual(self.g1s.remainingLives, 3)
        self.g1s.decreaseLife()
        self.assertEqual(self.g1s.remainingLives, 2)
        self.g1s.decreaseLife()
        self.assertEqual(self.g1s.remainingLives, 1)
        self.g1s.decreaseLife()
        self.assertEqual(self.g1s.remainingLives, 0)

    def testReturn(self):
        self.assertEqual(self.g1.guess('e'), True)
        self.assertEqual(self.g1.guessedChars, {'', 'e', 'n'})
        self.assertEqual(self.g1.currentStatus, '_e_____')
        self.g1.guess('b')
        self.assertEqual(self.g1.guess('b'), False)
        self.assertEqual(self.g1.guessedChars, {'', 'b', 'e', 'n'})
        self.assertEqual(self.g1.currentStatus, '_e_____')
        self.g1.guess('a')
        self.assertEqual(self.g1.guess('a'), True)
        self.assertEqual(self.g1.guessedChars, {'','a' ,'b', 'e', 'n'})
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        self.g1.guess('t')
        self.assertEqual(self.g1.guess('t'), True)
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'b', 'e', 't', 'n'})
        self.assertEqual(self.g1.currentStatus, '_e_a__t')
        self.g1.guess('u')
        self.assertEqual(self.g1.guess('u'), True)
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'b', 'e', 't', 'u', 'n'})
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.g1.guess('d')
        self.assertEqual(self.g1.guess('d'), True)
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'b', 'd', 'e', 't', 'u', 'n'})
        self.assertEqual(self.g1.currentStatus, 'de_au_t')
        self.g1.guess('f')
        self.assertEqual(self.g1.guess('f'), True)
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'b', 'd', 'e', 'f', 't', 'u', 'n'})
        self.assertEqual(self.g1.currentStatus, 'defau_t')
        self.g1.guess('l')
        self.assertEqual(self.g1.guess('l'), True)
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'b', 'd', 'e', 'f', 't', 'u', 'n', 'l'})
        self.assertEqual(self.g1.currentStatus, self.g1.secretWord)

    def testWord(self):
        self.assertEqual(self.g1w.test(), 'default')


if __name__ == '__main__':
    unittest.main()
