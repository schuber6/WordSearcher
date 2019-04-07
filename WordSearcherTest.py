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
