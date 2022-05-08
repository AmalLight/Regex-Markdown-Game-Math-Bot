#!/bin/python3

import sympy as sp
import numpy as np
import libs1 as l1
import libs5 as l5
import libs6 as l6


def load( data, i1, i2, commands ):
    if i1 == 20:
        i3 = int( commands[ 0 ] )-1

        if len( commands ) > 1: i4 = int( commands[ 1 ] )-1

        print( ' \t Matrice di Codominio on', i2+1, '.' )
        print( ' \t Matrice di Dominio   on', i3+1, '.' )

        if len( commands ) > 1: print( ' \t Matrice di Aiuto     on', i4+1, '.\n' )

        l6.load(  data, 18, i2, [] )
        i5 = len( data )-1

        if len( commands ) > 1: data[ i5 ][ 1 ] = data[ i5 ][ 1 ].dot( data[ i4 ][ 1 ] )

        data[ i5 ][ 1 ] = data[ i5 ][ 1 ].dot( data[ i3 ][ 1 ] )
        data[ i5 ][ 0 ] = 'from Inverse on ' + str( i2+1 ) +' * '+ str( i3+1 )

        if len( commands ) > 1: data[ i5 ][ 0 ] = data[ i5 ][ 0 ] +' , with help '+ str( i4+1 )

        print( ' \t Matrix added from inverse on', i2+1 )
        print( ' \t Matrix added with name', data[ i5 ][ 0 ] )
        print( ' \t Change Base on', i5+1 )
        l1.viewi( data, len( data )-1 )

    if i1 == 21:
        l1.clone( data, i2, 'from ' + str( i2+1 ) + ' to AutoValue' )

        matrix = data[ len( data )-1 ][ 1 ]
        data[ len( data )-1 ][ 1 ] -= ( sp.symbols( 'z' ) * np.identity( len( matrix ), dtype = int ) )

        detm = l6.det( matrix )
        
        l1.viewi( data, len( data )-1 )
        l1.remove( data, len( data )-1 )

        print( ' \t Det on', i2+1, ':', detm, 'done.' )
        print( ' \t AutoValue on', i2+1, 'done when det = 0 .\n' )

    if i1 == 22:
        i3 = int( commands[ 0 ] )-1
        elements = data[ i3 ][ 1 ][ 0,: ].tolist().copy()
        for el in elements:
            l1.clone( data, i2, 'from ' + str( i2+1 ) + ' to Kernel of Autovalue ' + str( el ) )

            i4 = len( data )-1
            matrix = data[ i4 ][ 1 ]
            matrix = matrix - ( el * np.identity( len( matrix ), dtype = int ) )
            matrix = np.c_[ matrix, [ 0 ] * len( matrix ) ]
            data[ i4 ][ 1 ] = matrix

            l1.viewi( data, i4 )
            l5.load( data, 14, i4, []  )

        print( ' \t Kernel Autovector on', i2+1, 'for', len( elements ), 'autovalues done.\n' )

            
