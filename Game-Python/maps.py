#!/bin/python3

from random import randint
from colors import Colors

class Maps:
    colors = Colors()

    # 0 per anonimo, 1 per acqua, 2 per buco, 3 per player.

    Know   = [[[ 3, 1, 999 ]]]
    Value  = [[1]]

    def __init__( self, n = 20, d = 3 ):
        self.n = 99 if n > 99 else n
        self.d = d
        self.m = (int( self.n/ self.d ) * self.n)

        iterator1 = iterator2 = 1

        for i in range(self.n-1):
            iterator1 = iterator1 + self.n
            self.Value += [[ iterator1 ]]

        for i1 in range(self.n):
            for i2 in range(self.n-1):
                iterator2 = iterator2 + 1
                self.Value[i1] += [ iterator2 ]
            iterator2 = iterator2 + 1

        for i1 in range(self.n-1): self.Know += [[[ 0, 1, self.n * self.n ]]]
        for i1 in range(self.n):
            for i2 in range(self.n-1):
                self.Know[i1] += [[ 0, 1, self.n * self.n ]]

        for i in range( self.m ):
            x = y = 0
            while( x == 0 and x == y ):
                x = randint( 0, (self.n - 1) )
                y = randint( 0, (self.n - 1) )
                self.Know[x][y][1] = 2

    def view_noColor( self, i=None ):
        if not i: Matrix = self.Value
        elif   i: Matrix = self.Know

        for i1 in range(self.n):
            print( "\n\t", end='' )
            for i2 in range(self.n):
                value = 0
                if not i: value = Matrix[i1][i2]
                elif   i: value = Matrix[i1][i2][i]
                print( value, end='' )
                print( " "*(4 - len( str( value ) ) ), end='' )
        print()
        print()

    def view_siColor( self, Matrix=None, i=0 ):
        if not Matrix: Matrix = self.Know

        for i1 in range(self.n):
            print( "\n\t", end='' )
            for i2 in range(self.n): #https://en.wikipedia.org/wiki/List_of_Unicode_characters
                if   Matrix[i1][i2][i] < 1:    self.colors.out( " ? ", 37, 31 ) # 0 -> anonimous
                elif Matrix[i1][i2][i] < 2:    self.colors.out( " ≈ ", 30, 96 ) # 1
                elif Matrix[i1][i2][i] < 3:    self.colors.out( " ≉ ", 37, 34 ) # 2
                else:                          self.colors.out( " ⊕ ", 32, 96 ) # 3 -> player
        print()
        print()

