#!/bin/python3

import tools as ts
import libs3 as l3

def createMatrix( data, name, array ):
    array = ''.join( array )

    if array and array.count( ',' ): array = array.split( ',' )
    else:                            array = [ array ]

    for i in range( len( array ) ):
        if array[ i ].count( '|' ): array[ i ] = array[ i ].split( '|' )
        else:                       array[ i ] = [ array[ i ] ]

    m = len( array )
    n = len( array[ 0 ] )

    if name and m and n and array and len( array ) == m:
        if not sum( [ 0 if len( el ) == n else 1 for el in array ] ):

            for x in range( m ):
                for y in range( n ): array[ x ][ y ] = ts.autoParse( array[ x ][ y ] )

            ts.added( data, name, array )
            print( '\t Matrix add on', len( data ), 'done.' )

def view( matrix ):
    m = len( matrix )
    n = len( matrix[ 0 ] )
    len_columns = []
    for y in range( n ): len_columns += [ max( [ len( str( el ) ) for el in matrix[:,y] ] ) ]
    for x in range( m ):
        for y in range( n ):
            numb = len_columns[ y ]-len( str( matrix[x][y] ) )
            if y  == 0: print( "   ", end = '' )
            if y < n-1: print( matrix[x][y], end = " "*numb +"   " )
            else:       print( matrix[x][y] )
    print()

