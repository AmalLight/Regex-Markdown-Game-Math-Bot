#!/bin/python3

from sys import argv
import importlib as lib
import libs1     as l1

data = []

list  = ' 1) clone  i stringa:                         \n'
list += ' 2) delete i:                               \n\n'

list += ' 3) swap  i R1 R2:                            \n'
list += ' 4) moltp i RX:                               \n'
list += ' 5) summ  i R1 R2:                            \n'
list += ' 6) turn  i:                                \n\n'

list += ' 7) subs  i var value:                        \n'
list += ' 8) gauss i:                                  \n'
list += ' 9) solve i:                                \n\n'

list += ' 10) App1 ( x, y, x, y ) name elements (|,):    \n'
list += ' 11) App2 ( x| y| w| z ) name elements (|,):  \n\n'

list += ' 12) add (0,..,0) to App.Linear i:              \n'
list += ' 13) Vector i elements (,):                   \n\n'

list += ' 14) Base per colonne ( auto    Solve ) i:      \n'
list += ' 15) Base per righe   ( no need Solve ) i:    \n\n'

list += ' 16) x^2, x, c elements (,):                    \n'
list += ' 17) Det..   i:                                 \n'
list += ' 18) Inverse i:                                 \n'
list += ' 19) Remove last column i:                    \n\n'

list += ' 20) Change Base i1 i2 i3 => i1^(-1)*(i3)*i2: \n\n'

list += ' 21) AutoValue i => Det( M - zI ):              \n'
list += ' *   AutoValues build Similar Matrix (Note)   \n\n'

list += ' 22) Kernel AutoVector i1 i2 => Kernel( M-iI ): \n'
list += ' *   M from i1, i from 1xN of i2.     (Note)      '

if not len( argv ) > 1:
    # print( '\033[0;36;40m{}'.format( list ) )
    print( list )
    input( '\n Press any key for finish: ' )
    print()

else:
    # print( ' \033[0;36;40m ', end= '' )
    out = filetoexec = None
    filetoexec = '/home/kaumi/' + argv[1]

    with open( filetoexec, 'r' ) as f:
        for out in f.readlines():
            if out[ :3 ] == 'sy ': l1.load( data, out[ 3: ] )

