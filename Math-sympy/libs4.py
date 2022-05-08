#!/bin/python3

import numpy as np
import libs1 as l1
import libs3 as l3
import libs5 as l5
import base6 as B6
import tools as ts


def clear( matrix ): return np.array( [ el for el in matrix if not Null( el.tolist() ) ] )
def reduce( data, i ):
    if not ( clear( data[ i ][ 1 ] ) == [] ): data[ i ][ 1 ] = clear( data[ i ][ 1 ] )
    else:                                     data[ i ][ 1 ] = np.array( [[ 0 ]]     )
    return data


def gaus( data, i ):
    m = len( data[ i ][ 1 ]      )
    n = len( data[ i ][ 1 ][ 0 ] )
    
    for m2 in range( m ):    
        num1 = num2 = x = y = flag = 0
        while x < m and y < n-1 and not flag:

            data[ i ][ 1 ] = order2( data[ i ][ 1 ] )

            num1 =           data[ i ][ 1 ].tolist()[ x   ][ y ]
            if x > 0: num2 = data[ i ][ 1 ].tolist()[ x-1 ][ y ]

            if x > 0 and num1 and num2: 
                flag = ts.checkVars( num2 )
                if not flag: l3.summ( data, i, x, x-1 )

            while not flag and not num1 and y < n-1:
                y = y + 1
                num1 = data[ i ][ 1 ].tolist()[ x ][ y ]
            num1 =     data[ i ][ 1 ].tolist()[ x ][ y ]

            if not flag: flag = ts.checkVars( num1 )
            # if not flag and num1 and not num1 == 1 and y < n-1: l3.molt( data, i, x )
            
            x = x + 1
        
    print( '\n\t Gauss from', i+1, 'done on', i+1 )
    l1.viewi( data, i )


def solve( data, i ):
    data = reduce( data, i )

    M = order1( data[ i ][ 1 ] )
    A = clear( M[ :,:-1 ] )
    B =        M[ :,-1  ].tolist()

    rA = len( A )       # rango A
    rB = len( M )       # rango AB
    n  = len( A[ 0 ] )  # numero di colonne

    var = ts.vars2()
    if not ( rA == rB ) or n > len( var ): return 0 # numero colonne esagerato
    sol = var[ : n ][ ::-1 ]                        # presa di alcune variabili
    val_row = -1                                    # riga nella matrice
    done = []

    for row in A:
        val_row = val_row + 1
        row = row.tolist()
        valid = countF( row ) 

        if not valid in done:
            row = row[ ::-1 ][ : valid ]
            val_col = 0

            for el in row:
                if el:
                    if row[ 1: ] == []:
                        sol[ valid-1 ] = B[ val_row ] / el
                        done = done + [ valid ]
                    else:
                        B[ val_row ] = B[ val_row ] - ( sol[ val_col ] * el )

                val_col = val_col + 1
                row = row[ 1: ]

    ts.added( data, 'from ' + str( i+1 ) + ' sol', [sol[ ::-1 ]] )
    print( ' \t Solve from', i+1, 'done on', len( data ) )
    l1.viewi( data, len( data )-1 )


def load( data, i1, i2, commands ):
    if  i1 == 7:
        i3 =                        commands[ 0  ]
        i4 = ts.autoParse( ''.join( commands[ 1: ] ) )
        l1.clone( data, i2, 'from ' + str( i2+1 ) + ' Subs' )
        l3.subs(  data, len( data )-1, i3, i4 )
        l1.viewi( data, len( data )-1 )

    elif i1 == 8: gaus( reduce( data, i2 ), i2 )
    elif i1 == 9: solve( data, i2 )

    else: l5.load( data, i1, i2, commands )


def Null(    arr ): return True if arr==[] else arr[0]==0 and Null( arr[ 1: ] )
def order1(  arr ): return np.array( sorted( arr.tolist(), key=countF ) )
def order2(  arr ): return np.array( sorted( arr.tolist(), key=countF, reverse=True ) )
def countF(  arr, i=1 ):
    if arr == []: return 0
    elif arr[ -1 ] == 0: return      countF( arr[ :-1 ], i+1 )
    else:                return max( countF( arr[ :-1 ], i+1 ), i )

