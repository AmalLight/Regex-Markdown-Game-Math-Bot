#!/bin/python3

from subprocess import call
from maps import Maps

class Interface:
    colors  = None
    maps    = None
    stringa = "Show Action"

    def __init__( self, n = 20 ):
        self.maps   = Maps( n )
        self.colors = self.maps.colors

    def show( self, stringa=None, Matrix=None ):
        if not Matrix:  Matrix  = self.maps.Know
        if not stringa: stringa = self.stringa
        else: self.stringa = stringa

        call('clear')
        self.maps.view_noColor( None )
        self.colors.out( "\t[[ " + self.stringa + " ]]", 30, 36 )
        print()
        self.maps.view_siColor( 0 )

    def aviable1( self, x,y ):
        if x >= 0 and y >= 0 and x < self.maps.n and y < self.maps.n: return True
        else: return False

    def sea( self, x,y ):
        if self.aviable1( x,y ): self.maps.Know[x][y][0] = 1

    def fail( self, x,y ):
        if self.aviable1( x,y ): self.maps.Know[x][y][0] = 2

    def person( self, x,y ):
        if self.aviable1( x,y ): self.maps.Know[x][y][0] = 3

