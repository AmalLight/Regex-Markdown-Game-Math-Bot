
-----------------------------------------------------------------------------

# JavaScript Modifier

1. List:

   - i = non-case-sensitive matching. uppercase and lowercase don’t matter.

   - g = global match. You attempt to find all matches instead of just returning the first match.
     the internal state of the regular expression stores where the last match was located,
     and matching is resumed where it was left in the previous match.

   - m = Multiline match. it treats the ^ and $ characters to match the beginning and the end
     of each line of the tested string. a newline character is determined by \n or \r.

   - u = unicode search. The regex pattern is treated as a unicode sequence.

   - y = sticky search.

   - s = single-line matching.
     The character will also match newline characters such as \r and \n.
     available in ES2018 and newer.

2. match => 'String'.match ( regex ) =>
   - find regex on string, way 1
   - return [ array for all matching ] if g is setted else ( only the first occurrence )
   
3. test => regex.test ( 'String' ) =>
   - test regex on string, way 2
   - return true if find match else false

4. exec => regex.exec ( 'String' ) =>
   - test regex on string, way 2, not return array
   - return only the first occurrence

5. toString => regex.toString () => classic use of toString ()

6. search =>
   - find regex on string
   - return -1 if not find else > index
   - return only the first occurrence

7. replace =>
   - 'String'.replace( regex, 'string2' )
   - find regex on string and replace it
   - replace only the first occurrence

8. split =>
   - 'String'.split( regex )
   - return array of splitted 'String', using the regex matching

-----------------------------------------------------------------------------

# Global  Matches

1. regex = /x+/g;

2. 'String' = 'yxxxyxyxx';

3. regex.exec( 'String' );
   - output : {0: 'xxx', index: 1, input: 'yxxxyxyxx' }

4. regex.lastIndex
   - output : 4

5. regex.exec( 'String' )
   - output : { 0: "x", index: 5, input: "yxxxyxyxx" }
   
6. regex.exec( 'String' )
   - output : { 0: "xx", index: 7, input: "yxxxyxyxx" }

7. regex.exec( 'String' )
   - output : null
   
8. 'String'.match( regex )
   - output : {0: 'xxx', index: 1, input: 'yxxxyxyxx' }
   
9. 'String'.match( regex )
   - output : ["xxx", "x", "xx"]

