#!/bin/python3

import numpy as np
import sympy as sp
import tools as ts

import libs1 as l1
import libs4 as l4

def swap( data, i2, i3, i4 ):
    tmp = data[ i2 ][ 1 ][ i3,: ].copy()
    data[ i2 ][ 1 ][ i3,: ] = data[ i2 ][ 1 ][ i4,: ]
    data[ i2 ][ 1 ][ i4,: ] = tmp
    print( ' \t Swap on', i2+1, 'done.' )

def molt( data, i2, i3 ):
    row = data[ i2 ][ 1 ][ i3,: ]
    pos = l4.countF( row.tolist() )
    div  = row.tolist()[ ::-1 ][ pos-1 ]
    data[ i2 ][ 1 ][ i3,: ] = ( 1 / div ) * data[ i2 ][ 1 ][ i3,: ]
    print( ' \t Molt on', i2+1, 'done.' )

def summ( data, i2, i3, i4 ):
    row1 = data[ i2 ][ 1 ][ i3,: ]
    row2 = data[ i2 ][ 1 ][ i4,: ]
    pos1 = l4.countF( row1.tolist() )
    molt = row1.tolist()[ ::-1 ][ pos1-1 ]
    div  = row2.tolist()[ ::-1 ][ pos1-1 ]
    data[ i2 ][ 1 ][ i3,: ] = ( ( -molt ) / div * data[ i2 ][ 1 ][ i4,: ] ) + data[ i2 ][ 1 ][ i3,: ]
    print( ' \t Summ on', i2+1, 'done.' )

def turn( data, i ):
    data[ i ][ 1 ] = data[ i ][ 1 ].T
    print( ' \t Turn on', i+1, 'done.' )

def subs( data, i, var, value ):
    data[ i ][ 1 ] = np.array( sp.Matrix( data[ i ][ 1 ] ).subs( var, value ) )
    print( ' \t Subs on', i+1, 'done.' )

def load( data, i1, i2, commands ):
    i3 = i4 = i5 = None

    if i1 in [ 3, 4, 5 ]: i3 = int( commands[ 0 ] )-1    
    if i1 in [ 3,    5 ]: i4 = int( commands[ 1 ] )-1

    if   i1 == 3:  swap( data, i2, i3, i4 )
    elif i1 == 4:  molt( data, i2, i3 )
    elif i1 == 5:  summ( data, i2, i3, i4 )
    elif i1 == 6:  turn( data, i2 )
    
    if i1 in [ 3, 4, 5, 6 ]: l1.viewi( data, i2 )
    else:       l4.load( data, i1, i2, commands )
