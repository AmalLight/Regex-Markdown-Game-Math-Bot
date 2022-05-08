
-----------------------------------------------------------------------------

# Modifiers

**maybe not for bash , i don't know**

1. for JavaScript
   - /.../_.test( '...' )
   - _ is modifire
   - ... is regular expression
   - '...' is a string to text

2. List:
   - g = global matching, which does not return after the first match.
   - m = Multiline matching to make ^ and $ match the start and end of a line
     instead of the start and the end of the whole string.
   - s = Single-line mode. The character . matches all characters including \n.
   - i = Case-insensitive matching.
   - x = Ignore whitespace characters. This option turns on free spacing mode.
   - u = Match with full Unicode.
   
3. **/re/i** in short is : **/re/i == /(r|R)(e|E)/** . It's equal to **{r, R}** ?

-----------------------------------------------------------------------------

# Execution in JavaScript

1. new RegExp( 'xy+' );
   - output : /xy+/
   - if you asking for the type of data using : typeof /xy+/
   - you will get : "object" , because JavaScript regular expressions are objects.

2. /xy+/.exec( 'yyxyy' );
   - output : {0: "xyy", index: 2, input: "yyxyy", length: 1}
   - exec executes a search returning information on a match.
   
3. /xy+/.test( 'yyxyy' );
   - output : true
   - test executes a search returning a Boolean indicating whether a match was found.

4. /xy+/.toString()
   - output : "/xy+/"
   - toString stringifies a regular expression.
   
**+ construct acts like a loop that matches as many y characters as it finds.**
**In other words, the y+ construct is greedy**

## Ways to accept regular expressions as arguments

- match executes a search in the string returning information on the upcoming match.
  It’s like the exec method on RegExp objects, exchanging the object and the argument.
  
- search executes a search in the string returning the index of the upcoming match.
  The returned index is -1 if the regex pattern cannot be found in the string.
  
- replace executes a search in the string and replaces the first match.

- split splits a string into substrings based on a specified regex pattern.

1.  s = 'xyyzxyzz';

2. s.match( /xy+/ );
   - output : { 0: "xyy", index: 0, input: "xyyzxyzz", length: 1 }
   
3. s.search( /xy+/ );
   - output : 0
   
4. s.replace( /xy+/, 'U' )
   - output : "Uzxyzz"
   
5. s
   - output : "xyyzxyzz"
   
6. s.split( /xy+/ )
   - output : ["", "z", "zz"]
   
## JavaScript , regex adding modifiers

1. x = new RegExp( 'x' )
   - output : /x/
   
2. xX = new RegExp( 'x', 'i' )
   - output : /x/i
   
3. x.test( 'XY' )
   - output : false
   
4. xX.test( 'XY' )
   - output : true

-----------------------------------------------------------------------------

