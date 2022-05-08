#!/bin/python3

from math import isnan
import numpy as np
import sympy as sp

a, b, c, d, e = sp.symbols( 'a b c d e' )
f, g, h,    j = sp.symbols( 'f g h   j' )
k, l,       o = sp.symbols( 'k l     o' )
p, q, r, s, t = sp.symbols( 'p q r s t' )
u, v, w,      = sp.symbols( 'u v w    ' )

def vars1(): return [ a, b, c, d, e, f, g, h, j, k, l, o, p, q, r, s, t, u, v, w ]
def vars2(): return [ a, b, c, d, e, f, g, h, j ]

def checkVars(  numb, arr = vars1() ):
    if arr == []:                              return 0
    elif str( numb ).count( str( arr[ 0 ] ) ): return 1
    else:                                      return checkVars( numb, arr[ 1: ] )

def sizeOfVars( numb, arr = vars2(), ritorno = [], i = 0 ):
    if arr == []:                              return                              ritorno
    elif str( numb ).count( str( arr[ 0 ] ) ): return sizeOfVars( numb, arr[ 1: ], ritorno + [ i ], i+1 )
    else:                                      return sizeOfVars( numb, arr[ 1: ], ritorno,         i+1 )

#-------------------------------------------------------------------------

def autoParse( inputs ):
    while inputs.count( '(' ): inputs = inputs.replace( '(', '' )
    while inputs.count( ')' ): inputs = inputs.replace( ')', '' )
    while inputs.count( ' ' ): inputs = inputs.replace( ' ', '' )
    return parse( inputs, 0, len( inputs ), '' )

def parse( inputs, il, ir, collect ):
    if inputs == '' or il >= ir: return tryget( collect )

    elif inputs[ il ] in [ '_', '^', '+', '-', '/', '*' ]:

        ir2 = len( collect )
        ir3 = len( inputs[ il+1: ] )

        first  = tryget( collect )
        second = parse( inputs[ il+1: ], 0, ir3, '' )

        if   inputs[ il ] == '_': return 1 if isnan( first ** ( 1/second ) ) else ( first ** ( 1/second ) )
        elif inputs[ il ] == '^': return first ** second
        elif inputs[ il ] == '+': return first +  second
        elif inputs[ il ] == '-': return first -  second
        elif inputs[ il ] == '/': return first /  second
        elif inputs[ il ] == '*': return first *  second

    else: return parse( inputs, il+1, ir, collect+inputs[ il ] )

#-------------------------------------------------------------------------

def tryget( inputs ):
    try: return sp.Rational( str( inputs ) )
    except: 
        try: return eval( str( inputs ) )
        except: return 0

def added( data, name, array ): data.extend( [[ name , np.array( array ) ]] )
