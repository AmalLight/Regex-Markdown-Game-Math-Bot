#!/bin/python3

import public

def debug( objectx, level=1 ):
    print( "\n" + str( objectx ) )
    input( "\t End Debug on level "+ str( level ) +" ?: " )

class AI:
    def __init__( self, maps, d=2, dead=4 ):
        [ self.n1, self.m1 ] = [ maps.n, maps.m ]
        self.n2 = self.n1**2
        self.dead = dead
        self.dr = { el : 0 for el in range( 1, self.n2+1 ) }

    def chose( self, maps, x,y, level=0 ):
        v = public.getv( maps, x,y )
        if not v: return None

        elsd = elsr = elsl = elsu = None
        [ els, size ] = [ None, 0 ]

        elsd = self.rdlu( maps, 'd', x+1 ,y, [], level+1, self.dead )
        if elsd: [ els, size ] = [ elsd, len( elsd ) ]
        else:
            elsr = self.rdlu( maps, 'r', x, y+1, [], level+1, self.dead )
            if elsr: [ els, size ] = [ elsr, len( elsr ) ]
            else:
                elsl = self.rdlu( maps, 'l', x, y-1, [], level+1, self.dead )
                if elsl: [ els, size ] = [ elsl, len( elsl ) ]
                else:
                    elsu = self.rdlu( maps, 'u', x-1, y, [], level+1, self.dead )
                    if elsu: [ els, size ] = [ elsu, len( elsu ) ]

        # Time of Machine Learning ( andrebbe fatto dopo ):

        if elsd or elsr or elsl or elsu:
            for el in els:
                if self.dr[ el ] == 0:
                   [ x,y ] = public.getxy( maps, el )
                   self.dr[ el ] = value = maps.Know[ x ][ y ][ 1 ]

                   if value == 1: self.n2 -= 1
                   if value == 2:
                       self.m1 -= 1
                       self.n2 -= 1
                       break

            return [ els, size ]
        return None


    def rdlu( self, maps, path, x,y, lista=[], level=1, dead=5 ):
        v = public.getv( maps, x,y )
        if not v or level>=dead: return None

        [ n1, tmpl, dict_ ] = [ self.n1, [], { 0 : None } ]
 
        if   path=='r': tmpl = [ el for el in range( v, public.getv( maps, x,n1-1 )+1     )]
        elif path=='d': tmpl = [ el for el in range( v, public.getv( maps, n1-1,y )+1, n1 )]
        elif path=='l': tmpl = [ el for el in reversed( range( public.getv( maps, x,0 ), v+1     ))]
        elif path=='u': tmpl = [ el for el in reversed( range( public.getv( maps, 0,y ), v+1, n1 ))]

        for el in tmpl:
            [ x,y ] = public.getxy( maps, el )
            value = maps.Know[ x ][ y ][ 0 ]
            clist = lista + tmpl[ :tmpl.index( el )+1 ]

            if value == 0: dict_[ len( clist ) ] = clist
            if value == 0 or value == 2: break

            elif value == 1:

                elsd = self.rdlu( maps, 'd', x+1, y, clist, level+1, dead )
                if elsd: dict_[ len( elsd ) ] = elsd
                else:
                    elsr = self.rdlu( maps, 'r', x, y+1, clist, level+1, dead )
                    if elsr: dict_[ len( elsr ) ] = elsr
                    else:
                        elsl = self.rdlu( maps, 'l', x, y-1, clist, level+1, dead )
                        if elsl: dict_[ len( elsl ) ] = elsl
                        else:
                            elsu = self.rdlu( maps, 'u', x-1, y, clist, level+1, dead )
                            if elsu: dict_[ len( elsu ) ] = elsu

        return dict_[ sorted( dict_ )[ 1 ] ] if len( dict_ ) > 1 else None


