
-----------------------------------------------------------------------------

# Python notation

1. import re

2. regex = re.compile ( "xk$" )

3. str1 = 'QxyxyyQxk'

4. print ( regex.search ( str1 ) )

5. print ( re.compile ( "xk\Z" ).search ( str1 ) )

6. result.group(), result.start(), result.end(), result.span()('xyy', 1, 4, (1, 4))

7. ==> Tutorial_script_2.py

**in Python you can use both**

-----------------------------------------------------------------------------

# Multiline  Matches

1. 'xx\nxXx\nxxxx'.match( '/^x+$/m' )
   - ["xx", index: 0, input: "xxxXxxxxx"]

2. 'xx\nxXx\nxxxx'.match( '/^x+$/mg' )
   - ["xx", "xxxx"]
   
3. 'xx\nxXx\nxxxx'.match( /^x+$/ )
   - null
   
-----------------------------------------------------------------------------

# ES6 Unicode Regular ExpressionsIn ES6
  - you can specify Unicode characters for matching.
  - A Unicode character is treated as one character regardless of the number of bytes the character occupies.

**'x'.codePointAt( 0 ).toString( 16 )"78"**

1. /\u{78}/.test( 'x' )
  - false
  
2. /\u{78}/u.test( 'x' )
  - true
  
**Another problem with Unicode characters is that their size in bytes may vary.**
**For instance, '\u{2ABCD}' is a Unicode character that cannot be represented using 4 bytes.**

-----------------------------------------------------------------------------

# Sticky  Matches

## Modifier
   - y = sticky search ==> Tutorial_script_1.html

1. regExp = /ab+/y
   - /ab+/y

2. 'ababbabbb'.match( regExp )
   - { 0:"ab", index: 0, input: "ababbabbb" }
   
3. regExp.lastIndex
   - 2
   
4. 'ababbabbb'.match( regExp )
   - { 0: "abb", index: 2, input: "ababbabbb" }
   
5. regExp.lastIndex
   - 5
   
6. 'ababbabbb'.match( regExp )
   - { 0:"abbb", index: 5, input: "ababbabbb" }
   
7. regExp.lastIndex
   - 9
   
8. 'ababbabbb'.match( regExp )
   - null
   
9. regExp.lastIndex
   - 0

10. 'ababbabbb'.match( regExp )
    - { 0: "ab", index: 0, input: "ababbabbb" }
    
11. regExp.lastIndex
    - 2

