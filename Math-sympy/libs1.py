#!/bin/python3

import libs2 as l2
import libs3 as l3
import tools as ts

def viewi( data, i ):
    print( ' \t index', i+1 )
    print( ' \t name', data[ i ][ 0 ], ':: \n' )
    l2.view( data[ i ][ 1 ] )

def clone( data, i, stringa ):
    ts.added( data, data[ i ][ 0 ] + ' ' + stringa, data[ i ][ 1 ] )
    print( ' \t Clone from',  i+1, 'on', len( data ) ,'done.' )
    viewi( data, len( data )-1 )

def remove( data, i ):
    data.remove( data[ i ] )
    print( ' \t Remove on', i+1, 'done.' )

def load( data, commands ):
    while commands.count( '  ' ): commands = commands.replace( '  ', ' ' )

    i1 = int( commands.split( ' ' )[ 0 ] )
    i2 = i3 = None
    if i1  > 1: i2 = commands.split( ' ' )[ 1 ]
    if i1 == 3: i3 = commands.split( ' ' )[ 2 ]

    if not ( i1 in [ 10, 11, 16 ] ): i2 = int( i2 )-1

    if   i1 == 1: clone(  data, i2, i3 )
    elif i1 == 2: remove( data, i2     )
    
    else: l3.load( data, i1, i2, commands.split( ' ' )[ 2: ] )
