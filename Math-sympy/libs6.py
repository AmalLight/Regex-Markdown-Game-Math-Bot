#!/bin/python3

import numpy as np
import libs1 as l1
import libs3 as l3
import libs7 as l7
import tools as ts


def det( matrix ):
    [ value, sign ] = [ 0, 1 ]
    m = len( matrix )
    n = len( matrix[ 0 ] )

    if n == m:
        if n == 2:
            a = matrix[ 0 ][ 0 ]
            b = matrix[ 0 ][ 1 ]
            c = matrix[ 1 ][ 0 ]
            d = matrix[ 1 ][ 1 ]
            return ( a*d ) - ( b*c )

        else:
            matrix2 = matrix[ :,1: ]
            for i in range( m ):

                cost = matrix[ i ][ 0 ]
                if cost:

                    matrix3 = np.delete( matrix2, i, 0 )
                    value  += ( cost * det( matrix3 ) * ( (-1) ** i ) )
            
            return value
    else: return None


def load( data, i1, i2, commands ):
    if i1 == 17: print( ' \t Det on', i2+1, det( data[ i2 ][ 1 ] ), 'done.\n' )
    
    elif i1 == 18:
        m = len( data[ i2 ][ 1 ]      )
        n = len( data[ i2 ][ 1 ][ 0 ] )

        if n == m:
            l1.clone( data, i2, 'from ' + str( i2+1 ) + ' to Inverse' )
            detm = det( data[ i2 ][ 1 ] )

            for i3 in range( m ):
                for i4 in range( n ):

                    sign = ( -1 ) ** ( i3+1 + i4+1 )

                    tmp = data[ i2 ][ 1 ]
                    tmp = np.r_[ tmp[ :i3, : ] , tmp[ i3+1:, : ] ]
                    tmp = np.c_[ tmp[ :, :i4 ] , tmp[ :, i4+1: ] ]

                    data[ len( data )-1 ][ 1 ][ i3 ][ i4 ] = sign * det( tmp ) / detm

            print( ' \t Det on', i2+1, ':', detm, 'done.' )
            l3.turn( data, len( data )-1 )
            print( ' \t Inverse from', i2+1, 'on', len( data ) )
            l1.viewi( data, len( data )-1 )

    elif i1 == 19:
        l1.clone( data, i2, 'from ' + str( i2+1 ) + ' to Remove_last' )
        data[ len( data )-1 ][ 1 ] = data[ len( data )-1 ][ 1 ][ :,:-1 ]
        print( ' \t Remove last column on', i2+1, 'done.' )
        l1.viewi( data, len( data )-1 )

    else: l7.load( data, i1, i2, commands )

