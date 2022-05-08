import re

# Notice the r in front of the string. In Python, this denotes a raw string.

# Raw string literals are string literals that are designed to make it easier,
# to include nested characters like quotation marks and backslashes,
# that normally have meanings as delimiters and escape sequence starts.

print ( 'INTRO' )

regex = re.compile ( r'xy+' )

# not worker = '/xy+/' , '/\rrxy+/' , '/\\rxy+/'

str1 = 'QxyxyyQxk'

result = regex.search( str1 )

print ( result.group(), result.start(), result.end(), result.span() )

result = regex.match( "xyyQ" )

print ( regex.match( "xyyQ" ) )

print ( result.group() )

print ( '' )
# ------------------------------------------------------------------------
# Global  Matches

print ( 'FIRST step' )

str1 = 'QxyxyyQxkxyyyy'

print ( re.findall( regex , str1 ) )

print ( '' )
# ------------------------------------------------------------------------

print ( '2° step' )

iterator = re.finditer ( 'xy+', 'QxyxyyQxyyyQ' )

print ( iterator )

for matchNum, match in enumerate(iterator):

    print ( match.group(), match.span() )

print ( '' )
# ------------------------------------------------------------------------

print ( 'LAST step' )

regex = r"ab+"

test_str = "ababb"

matches = re.finditer ( regex , test_str )

for matchNum, match in enumerate( matches ):

    matchNum = matchNum + 1
    
    print (
    
        "Match {matchNum} was found at {start}-{end}: {match}".format (
        
           matchNum = matchNum,start = match.start(),end = match.end(),match = match.group()
        )
    )

