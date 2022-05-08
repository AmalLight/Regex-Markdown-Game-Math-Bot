#!/bin/python3

import tools as ts


def splitstring( el ):
    strel = str( el ).replace( '-', '+-' )
    if strel and strel[ 0 ] == '+' : strel = strel[ 1: ]
    return strel.split( '+' )


def load( solution, tipo ):
    [ pos1, pos2 ] = [ 0, 0 ]
    [ sol, dict1 ] = [ [], { -1 : {} } ]

    number_var = len( ts.sizeOfVars( solution ) ) + 1
    number_sol = len( solution )
    for i in range( number_var ): sol = sol + [ [ None ] * number_sol ]

    for el1 in solution:
        for el2 in splitstring( el1 ):

            el = ts.autoParse( el2 )

            ritorno = ts.sizeOfVars( el2 )
            if ritorno:
                for index in ritorno:
                    var = ts.vars2()[ index ]
                    if not index in dict1:  dict1[ index ] = {}
                    dict1[ index ][ pos1 ] = el / var
            else:   dict1[ -1 ][ pos1 ] =    el

        pos1 = pos1 + 1

    dict2 = { key : dict1[ key ] for key in sorted( dict1.keys() ) }

    for pos1 in range( number_sol ):
        n_var = 0
        for key in dict2:
            if not pos1 in dict2[ key ]: dict2[ key ][ pos1 ] = 0
            sol[ n_var ][ pos1 ] = dict2[ key ][ pos1 ]
            n_var = n_var + 1

    print( ' \t Base', tipo, sol )