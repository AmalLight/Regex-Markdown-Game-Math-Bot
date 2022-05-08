#!/bin/python3

import time, socket, os, threading, midori, erika

# come or
def containsO( x, y ):
    for el in y:
        if x.count( el ):
            return True
    return False

# come and
def containsA( x, y ):
    for el in y:
        if not x.count( el ):
            return False
    return True

class IRC:
    serv = 'marte.ircgate.it'
    pre_name = 'Ninja01_'
    port = 6667
  
    def __init__( self ):
        self.chan = self.admin = None
        self.name = self.pre_name

        self.irc = socket.socket()
        self.irc.connect( ( self.serv, self.port ) )

        self.sendSR( ' '.join( [ "USER", self.name, self.name, self.name, ":" + self.name, "\n" ] ))
        self.sendSR( ' '.join( [ "NICK",     self.name, "\n" ] ))
        self.sendSR( ' '.join( [ "UMODE -c", self.name, "\n" ] ))
        self.connect = True

        time.sleep( 0.1 )
        print( 'connect to serv:', self.serv, 'on port:', self.port )
        print( 'clear reader...' )

        first = str( self.irc.recv( 2048 * 200 ).decode( "UTF-8" ) )
        print( first )

        if first.count( 'PING :' ):
            pong = first[ first.index( 'PING :' ) : ]
            pong = pong[ : pong.index( '\n' ) ].replace( 'PING', 'PONG', 1 )
            self.sendSR( pong )
            print( pong )
     
        time.sleep( 4 )
        print( str( self.irc.recv( 2048 * 200 ).decode( "UTF-8" ) ) )

    def sendSR( self, msg ):
         self.irc.send( msg.encode() )
         time.sleep( 1 )

    def sendAD( self, msg ):
        if self.admin: self.sendSR( ' '.join( [ "NOTICE",  self.admin, msg, "\n" ] ) )

    def sendCH( self, msg ):
        if self.chan:  self.sendSR( ' '.join( [ "PRIVMSG", self.chan,  msg, "\n" ] ) )

    def outCH( self ):
        if self.chan:
            self.sendSR( ' '.join( [ "PART", self.chan, "\n" ] ))
            print( 'out to the chan:', self.chan )
        self.chan = None

    def joinCH( self, chan ):
        self.outCH()
        self.chan = chan
        self.sendSR( ' '.join( [ "JOIN", self.chan, "\n" ] ))
        print( 'connect to chan:', self.chan )

    def ping( self ):
        while self.connect:
            try:
                time.sleep( 100 )
                self.sendSR( ' '.join( [ "PING", "\n" ] ))
                print( ' ping done ..' )
            except: break

    def main( self ):
        threading.Thread( target=self.ping, args=() ).start()
        print( 'ping started ..' )
        midori.init()
        print( 'midori init ...' )
        print( midori.getForMe( 'it', 'en', 'primo caricamento' ) )
        print( 'ready read ....' )

        while self.connect:

            text = ''
            try: text = str( self.irc.recv( 2048 ).decode( "UTF-8" ) )
            except: None

            if text.count( ':' ) >=2 and text.count( '!' ):

                text = text[ text.index( ':' )+1 : ]
                after = mittente = text[ : text.index( '!' ) ]
                text = text[ text.index( ':' )+1 : ]

                wiki = gog = chan = False

                print( ' ' + mittente + ' write: ' + text, end='' )

                if not after == self.name:

           #----------------------------------------------------------------------------------------------

                    if containsO( text, [ 'su_' ] ) and mittente == self.admin:
                        after = ''
                        for t in text.split():
                             if t.count( 'su_' ): after = t[ t.index( 'su_' )+3 : ]

                        if after: text = text.replace( 'su_' + after, '' )
                        if not after: after = mittente

           #----------------------------------------------------------------------------------------------

                    if containsO( text, [ 'print' ] ):
                        self.sendCH( after +': '+ text.replace( 'print', '' ))

           #----------------------------------------------------------------------------------------------

                    elif containsA( text, [ 'myadmin', 'join_' ] ):
                        chan = ''

                        for t in text.split():
                             if t.count( 'join_' ): chan = t[ t.index( 'join_' )+5 : ]

                        if input( ' dai a: '+ after +' il chown su: '+ self.pre_name +': ' ) == 'si':
                            self.admin = after
                            self.name = self.pre_name + after
                            self.sendSR( ' '.join( [ "NICK", self.name, "\n" ] ))
                            self.sendAD( 'su chown '+ self.name )

                        if chan:
                            self.joinCH( chan )
                            self.sendAD( 'I \'am ready' )

           #----------------------------------------------------------------------------------------------

                    elif containsA( text, [ 'gog_', '.' ] ):
                        i1 = text.index( 'gog_' )
                        i2 = text.index( '.' )
                        if i2 > i1:
                            gog = text[ i1+4 : i2 ]
                            self.sendCH( after +': '+ erika.connectGOG( gog ))

           #----------------------------------------------------------------------------------------------

                    elif containsA( text, [ 'wiki_', '.' ] ):
                        i1 = text.index( 'wiki_' )
                        i2 = text.index( '.' )
                        if i2 > i1:
                            wiki = text[ i1+5 : i2 ]
                            self.sendCH( after +': '+ erika.connectWIKI( wiki ))

           #----------------------------------------------------------------------------------------------

                    elif containsO( text, [ 'sleep' ] ) and mittente == self.admin:
                        self.sendCH( after + ' bye bye' )
                        print( ' pkill firefox' )
                        os.system( 'pkill firefox' )
                        self.connect = False

                        time.sleep( 1 )
                        print( ' pkill py' )
                        os.system( 'pkill py' )

           #----------------------------------------------------------------------------------------------

                    elif containsO( text, [ 'trl' ] ):
                        out = text.replace( 'trl', '' )
                        sl = tl = st = w = c = trl = save = ''

                        for o in out.split():
                             if   o.count( '.s' ): sl = o[ o.index( '.s' )+2 : ]
                             elif o.count( '.t' ): tl = o[ o.index( '.t' )+2 : ]

                        out = out.replace( '.s'+ sl, '' )
                        out = out.replace( '.t'+ tl, '' )

                        #debug empty:
                        if not sl: sl = 'it'
                        if not tl: tl = 'en'
                        if out.count( 'rev' ):
                            tm = sl
                            sl = tl
                            tl = tm
                            out = out.replace( 'rev', '' )

                        #debug wrong:
                        while out.count( '  ' ): out = out.replace( '  ', ' ' )
                        while out and out[0 ] == ' ': out = out[ 1 :  ]
                        while out and out[-1] == ' ': out = out[ : -1 ]

                        print( ' ricevuta st di traduzione, inizio midori' )
                        save = midori.getForMe( sl, tl, out )
                        print( ' midori finito' )

                        if save: self.sendCH( after +': '+ save    )
                        else:    self.sendCH( mittente +': Text wrong datas .. ' )
irc = IRC()
irc.main()
irc.irc.close()

