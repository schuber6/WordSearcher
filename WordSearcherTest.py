# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 17:02:59 2019

@author: huber.288
"""

import unittest
from WordSearcher import WordSearcher


class WordSearchTest(unittest.TestCase):
    def setup(self):
        self.WordSearcher = WordSearcher()
        self.puzzle = '''BONES,KHAN,KIRK,SCOTTY,SPOCK,SULU,UHURA
U,M,K,H,U,L,K,I,N,V,J,O,C,W,E
L,L,S,H,K,Z,Z,W,Z,C,G,J,U,Y,G
H,S,U,P,J,P,R,J,D,H,S,B,X,T,G
B,R,J,S,O,E,Q,E,T,I,K,K,G,L,E
A,Y,O,A,G,C,I,R,D,Q,H,R,T,C,D
S,C,O,T,T,Y,K,Z,R,E,P,P,X,P,F
B,L,Q,S,L,N,E,E,E,V,U,L,F,M,Z
O,K,R,I,K,A,M,M,R,M,F,B,A,P,P
N,U,I,I,Y,H,Q,M,E,M,Q,R,Y,F,S
E,Y,Z,Y,G,K,Q,J,P,C,Q,W,Y,A,K
S,J,F,Z,M,Q,I,B,D,B,E,M,K,W,D
T,G,L,B,H,C,B,E,C,H,T,O,Y,I,K
O,J,Y,E,U,L,N,C,C,L,Y,B,Z,U,H
W,Z,M,I,S,U,K,U,R,B,I,D,U,X,S
K,Y,L,B,Q,Q,P,M,D,F,C,K,E,A,B'''
        self.WordSearcher.LoadPuzzle(self.puzzle)

    def test_RecognizesWords(self):
        self.setup()
        words = self.WordSearcher._words
        self.assertEqual(words, ['BONES', 'KHAN', 'KIRK', 'SCOTTY',
                                 'SPOCK', 'SULU', 'UHURA'])

    def test_LoadsPuzzleInto2dList(self):
        self.setup()
        puzzle = self.WordSearcher._puzzle
        self.assertEqual(puzzle[0][0], 'U')
        self.assertEqual(puzzle[5][2], 'O')
        self.assertEqual(puzzle[3][5], 'E')

    def test_FindsHozinallyForwards(self):
        self.setup()
        Answers = self.WordSearcher.solve()
        self.assertEqual(Answers['SCOTTY'], [(0, 5), (1, 5), (2, 5),
                         (3, 5), (4, 5), (5, 5)])
    
    def test_FindsHorizontallyBackwards(self):
        self.setup()
        Answers = self.WordSearcher.solve()
        self.assertEqual(Answers['KIRK'], [(4, 7), (3, 7), (2, 7), (1, 7)])

    def test_FindsVerticallyDownwards(self):
        self.setup()
        Answers = self.WordSearcher.solve()
        self.assertEqual(Answers['BONES'], [(0, 6), (0, 7), (0, 8),
                         (0, 9), (0, 10)])

    def test_FindsVerticallyUpwards(self):
        self.setup()
        Answers = self.WordSearcher.solve()
        self.assertEqual(Answers['KHAN'], [(5, 9), (5, 8), (5, 7), (5, 6)])

    def test_FindsDiagonally(self):
        self.setup()
        Answers = self.WordSearcher.solve()
        self.assertEqual(Answers['SPOCK'], [(2, 1), (3, 2), (4, 3),
                         (5, 4), (6, 5)])
        self.assertEqual(Answers['SULU'], [(3, 3), (2, 2), (1, 1), (0, 0)])
        self.assertEqual(Answers['UHURA'], [(4, 0), (3, 1), (2, 2),
                         (1, 3), (0, 4)])

    def test_LoadsPuzzleFromFile(self):
        self.WordSearcher = WordSearcher()
        self.WordSearcher.LoadFromFile('Puzzle1.txt')
        puzzle = self.WordSearcher._puzzle
        self.assertEqual(puzzle[0][0], 'U')
        self.assertEqual(puzzle[5][2], 'O')
        self.assertEqual(puzzle[3][5], 'E')

    def test_OutputFormat(self):
        self.setup()
        _ = self.WordSearcher.solve()
        answer = '''BONES: (0,6),(0,7),(0,8),(0,9),(0,10)
KHAN: (5,9),(5,8),(5,7),(5,6)
KIRK: (4,7),(3,7),(2,7),(1,7)
SCOTTY: (0,5),(1,5),(2,5),(3,5),(4,5),(5,5)
SPOCK: (2,1),(3,2),(4,3),(5,4),(6,5)
SULU: (3,3),(2,2),(1,1),(0,0)
UHURA: (4,0),(3,1),(2,2),(1,3),(0,4)'''
        self.assertEqual(self.WordSearcher.Output(), answer)
