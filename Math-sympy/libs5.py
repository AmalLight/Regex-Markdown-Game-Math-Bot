#!/bin/python3

import numpy as np
import libs6 as l6
import libs4 as l4
import libs3 as l3
import libs2 as l2
import libs1 as l1
import tools as ts
import base6 as B6

def load( data, i1, i2, commands ):
    if i1 == 10 or i1 == 11:
        l2.createMatrix( data, i2, commands )

        if i1 == 11: l3.turn( data, len( data )-1 )
        print( ' \t App. Linear created on', len( data ) )
        l1.viewi( data, len( data )-1 )

    elif i1 == 12:
        l1.clone( data, i2, 'from ' +str( i2+1 ) +' to Kernel or Image' )

        matrix = data[ i2 ][ 1 ]
        data[ len( data )-1 ][ 1 ] = np.c_[ matrix, [ 0 ] * len( matrix ) ]

        print( ' \t added (0,..,0) to App. Linear from', i2+1 )
        l1.viewi( data, len( data )-1 )

    elif i1 == 13:
        l1.clone( data, i2, 'from ' + str( i2+1 ) + ' to Vector' )
        l2.createMatrix( data, 'tmp vector', commands )

        vector = data[ len( data )-1 ][ 1 ]
        l1.remove( data, len( data )-1 )
        
        matrix = data[ i2 ][ 1 ]
        data[ len( data )-1 ][ 1 ] = np.c_[ matrix, vector.T ]
        
        print( ' \t Vector from', i2+1 )
        l1.viewi( data, len( data )-1 )

    elif i1 == 14:
        l4.gaus(  data, i2 )
        l4.solve( data, i2 )
        if len( data )-1 > i2:
            B6.load( data[ len( data )-1 ][ 1 ][ 0,: ], 'Base' )
            l1.remove( data, len( data )-1 )
            print( ' \t Base per colonne on', i2+1, 'done.\n' )

    elif i1 == 15:
        print( ' \t Base per righe on', i2+1, 'done.' )
        for row in data[ i2 ][ 1 ]: print( '\t colonna:', row.tolist() )
        print()

    elif i1 == 16:
        arr = ( i2 + ''.join( commands ) )[ :-1 ].split( '|' )
        xx, x, y = ts.autoParse( arr[ 0 ] ), ts.autoParse( arr[ 1 ] ), ts.autoParse( arr[ 2 ] )

        delta = ( x*x ) -  ( 4*xx*y )
        sol1  = ts.tryget( ( -x + delta**( 1/2 ) ) / 2*xx )
        sol2  = ts.tryget( ( -x - delta**( 1/2 ) ) / 2*xx )
                
        ts.added( data, 'XX X c', [[ sol1, sol2 ]] )
        print(  ' \t Ask XX X c', str( arr ) )
        print(  ' \t Sol', '( x +', -sol1, ') * ( x +', -sol2, ')', 'done.' )
        print(  ' \t Solution list added on', len( data ) )
        l1.viewi( data, len( data )-1 )

    else: l6.load( data, i1, i2, commands )
