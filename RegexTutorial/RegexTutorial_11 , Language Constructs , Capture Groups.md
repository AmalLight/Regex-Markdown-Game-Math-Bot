
-----------------------------------------------------------------------------

# Concatenating Advanced Language Constructs

1. Simple Contact => /[^a-z][^a-z]/ === /casa mia/ == /casa.mia/
   - but nothing more
   
2. '[(1+2)*3]^2'.match( /[(1+2)*3]^2/ )
   - null
   
3. '[(1+2)*3]^2'.match( /\[\(1\+2\)\*3\]\^2/ )
   - [ '[(1+2)*3]^2' ]
   - but nothing more
   
4. Some languages such as Perl and PHP provide the \Q and \E
   they are special characters able to write any characters unescaped.

   - $re = '/\Q[(1+2)*3]^2\E/';
   - $str = '[(1+2)*3]^2';

   - preg_match_all($re, $str, $matches, PREG_SET_ORDER, 0);

   - [ '[(1+2)*3]^2' ]
   - but nothing more
   
5. in JavaScript:
   - \Q[casa mia]\E|0
   - [ '[casa mia]' , '0' ]
   - \E is meaning the END of \Q

-----------------------------------------------------------------------------

# Substring Extraction from Regular Expressions

- To test whether a string matches a search expression
- To find some characters in a string
- To replace substrings in a string matching a regex
- To process and format user input
- To extract information from server logs, configura-tion files, and text files
- To validate input in web applications and in the terminal

## Capture Groups => (x) , remember Prolog ?

1. Capture groups cannot be defined inside character classes

### Example exercise :

- find price in `Price: €19.00`

1. take a group : /(\€[\d]+.[\d]+$)/

2. require a group for pass over , using ?
   - ? like explicit AND
   - /(\€[\d]+.[\d]+$)?\d+.\d+/ , maybe it's not correct . \d+.\d+ searches all test
   
3. set correctly the groups using more `(` and more `)`
   - example : `/^Price: (([€\$])(\d\d\.\d\d))$/`

4. you will get:
   - 1 a full price
   - 2 the currency
   - 3 the numeric price

-----------------------------------------------------------------------------
