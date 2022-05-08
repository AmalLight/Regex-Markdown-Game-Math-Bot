#!/bin/python3

import time, public
from interface import Interface
from ai import AI

class Game:
    #maps, stringa used from interface
    colors = interface = None
    x = y = n = 0
    
    def __init__( self, n = 20 ):
        self.interface = Interface( n )
        self.n  = self.interface.maps.n
        self.m  = self.interface.maps.m
        self.ai = AI( self.interface.maps )

        self.setString( "START" )
        while True:
            self.interface.show()
            commands = input( "\tEnter your commands: " )
            self.action( commands )

    def getString( self ): return self.interface.stringa
    def setString( self, stringa="None" ): self.interface.stringa = stringa

    def mvxy( self, v, t=0.2 ):
        vxy = public.getv( self.interface.maps, self.x, self.y )
        b1 = vxy and public.getxy( self.interface.maps, v )
        b2 = vxy and ( v in [ (vxy + 1      ), (vxy - 1      ) ] )
        b3 = vxy and ( v in [ (vxy + self.n ), (vxy - self.n ) ] )

        if b1 and ( b2 or b3 ):
           [ x2,y2 ] = public.getxy( self.interface.maps, v )

           if self.interface.maps.Know[x2][y2][1] < 2:
              time.sleep( t )
              x3 = self.x
              y3 = self.y
              self.interface.sea( self.x, self.y )
              self.interface.person( x2,y2 )
              self.x = x2
              self.y = y2

              if self.interface.maps.Value[x2][y2] == (self.n * self.n):
                 self.interface.sea( self.x, self.y )
                 self.x = self.y = 0
                 self.interface.person( self.x, self.y )

           elif self.interface.maps.Know[x2][y2][1] < 3:
                self.interface.fail( x2,y2 )
                if self.interface.maps.Value[ x2 ][ y2 ] == (self.n * self.n):
                   self.interface.sea( self.x, self.y )
                   self.x = self.y = 0
                   self.interface.person( self.x, self.y )

    def action( self, commands ):
        if commands == 'mv':
            self.setString( 'move from robot' )
            while( True ):
                path = self.ai.chose( self.interface.maps, self.x, self.y )

                if not path:
                    self.interface.sea( self.x, self.y )
                    self.x = self.y = 0
                    self.interface.person( self.x, self.y )
                    self.setString( ',,,Not-Strong-Enough=Over.' )
                    self.interface.show()
                else:
                    [ els, size ] = [ path[ 0 ], path[ 1 ] ]
                    for el in els:
                        self.mvxy( el )
                        self.setString( 'els:' + str( els ) + '; size: ' + str( size ) )
                        self.interface.show()

                if ( self.x == self.y == 0 ): break

        elif 'mv' in commands:
            self.setString( 'move from command line' )
            for el in commands.split():
                if not 'mv' in el and int( el ) in self.ai.dr:
                    self.mvxy( int( el ) )
                    self.interface.show()

        elif commands == 'exit': exit()

        elif commands == 'stat1':
            print()
            print( "\t n:"           , self.ai.n1 )
            print( "\t d:"           , self.interface.maps.d )
            print( "\t n.remaining:" , self.ai.n2 )
            print( "\t m.remaining:" , self.ai.m1 )
            print( "\t pg.x:"        , self.x )
            print( "\t pg.y:"        , self.y )
            print( "\t pg.v:"        , self.interface.maps.Value[ self.x ][ self.y ])
            print( "\t K.rows:"      , len( self.interface.maps.Know     ))
            print( "\t K.columns:"   , len( self.interface.maps.Know[0]  ))
            print( "\t V.columns:"   , len( self.interface.maps.Value[0] ))
            print( "\t V.rows:"      , len( self.interface.maps.Value    ))
            print()
            commands = input( "\tPress any key for reload. " )

        elif 'stat2' in commands:
            if len( commands.split() ) > 1:
                print()
                for key in commands.split():
                    if not key == "stat2" and int(key) in self.ai.dr:
                        print("\t dict key", key, ":", self.ai.dr[ int(key) ])
                print()

            else: print( "\n\t DICT\n", self.ai.dr, "\n" )
            commands = input( "\tPress any key for reload. " )

        elif commands == 'view':
            self.interface.maps.view_noColor( 2 )
            commands = input( "\tPress any key for reload. " )

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
game = Game() #Main

