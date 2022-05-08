#!/bin/python3

import os, time, threading
from pynput.keyboard import Key, Controller

keyboard = Controller()

def inject( sl, tl, stringa ):
    sinj = 'https://translate.google.it/#view=home&op=translate&sl={}&tl={}&text={}'.format( sl, tl, stringa )
    print( ' inject: '+ sinj +'.' )
    return sinj

def newF1(): os.system( "firefox https://translate.google.it" )
def newF2(): os.system( "firefox https://translate.google.it" )
def newJN( sl, tl, st ): os.system( 'firefox "'+ inject( sl, tl, st ) +'"' )

def keyPress( v ):
    keyboard.press( v )
    keyboard.release( v )
    time.sleep( 0.1 )

def init():
    threading.Thread( target=newF1, args=() ).start()
    time.sleep( 5 )
    threading.Thread( target=newF2, args=() ).start()
    time.sleep( 5 )

def stop( stringa ):
    print( ' step5 kill tab in newJN, done.' )
    with keyboard.pressed( Key.ctrl_l ):
        keyboard.press( 'w' )
        keyboard.release( 'w' )
        return stringa

def getForMe( sl, tl, st ):
    if sl and tl and st:
        st = st.replace( '\n', '' ).replace( '\r', '' ).replace( ' ', '%20' )

        threading.Thread( target=newJN, args=( sl, tl, st ) ).start()
        time.sleep( 2.2 )

        print( ' input:', str( ( sl, tl, st )) )
        print( ' output st:', st.replace( '%20', ' ' ) )
        st = st.replace( '%20', ' ' )

        keyPress( Key.tab )
        print( ' step1 tab for one, done.' )

        with keyboard.pressed( Key.ctrl_l ): keyPress( 'a' )
        print( ' step2 ctrl+A, done.' )

        sel = os.popen( 'xsel' ).read()
        lista = sel.split( '\n' )
        print( ' step3 list from sel, sel: '+ sel  +' , done.' )
        print( ' step4 st len: '+ str( len( st ) ) +' , done.' )

        for s in lista:
            if s.count( str( len( st ) )+'/' ):
                if not s == lista[-1]:
                    print( ' step5 find translate, done.' )
                    return stop( lista[ lista.index( s )+1 ] )

        print( ' step5 no find translate, error.' )
        return stop( '' )

