#!/bin/python3

import requests, os, threading

wiki= 'https://it.wikipedia.org/wiki'
gog=  'https://www.google.it/search'

def cure1( string ): return string.replace( ';', ' ' ).replace( '&#', '' )
def cure2( string ): return string.replace( '\\', '' )
    
#-----------------------------------------------------------------------------------------------------

def connectWIKI( page ):
    save = str( requests.get( wiki +'/'+ page.replace( ' ', '_' ) ).content.decode( 'UTF-8' ) )
    export = ''
    opens = False

    for s in save:
        if   s == '<' and not opens: opens = True
        elif s == '>' and opens: opens = not opens
        elif not opens: export += s

    if save and save.count( 'Indice' ):

        export = export[ : export.index( 'Indice' ) ]
        while export and export[-1]=='\n': export = export[:-1]

        lista = export.split( '\n' )
        if lista: return cure1( lista[-1].replace( '\n', ' ' ) )

    return 'NO'

#-----------------------------------------------------------------------------------------------------

def connectGOG( page ):
    req = requests.get( gog, params={ 'q' : page +'+wikipedia' }, )
    text = str( req.content )

    end= ' - Wikipedia<'
    num= text.count( end )
    lista = []

    for i1 in range( num ):
        i2 =  text.index( end )
        tmp = text[ : i2 ]
        out = ''
        for c in reversed( tmp ):
            if c == '>': break
            else: out = c + out

        lista += [ cure1( cure2( out ) ) ]
        text = text[ i2 + len( end ) : ]

    return str( lista )

