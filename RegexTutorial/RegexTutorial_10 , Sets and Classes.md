
-----------------------------------------------------------------------------

# Sets and Classes

## Sets

### Inclusion

1. /<[01]>/ in Perl 6            = [0-1]
2.  /[01]/ in all other dialects = [0-1]

3. /[01234567]/ for an octal                    == [01234567]
4. /[0123456789abcdefABCDEF]/ for a hexadecimal == [0-9]|[a-f]|[A-F]

5. /<[0..7]>/ in Perl 6           == [01234567]
6.  /[0-7]/ in all other dialects == [01234567]

7. union for all : /[0-9]|[a-f]|[A-F]/ == [0123456789abcdefABCDEF]
   - [0-9] == [01234567]
   - [a-f] == [abcdef]
   - [A-F] == [ABCDEF]

8. /<[0..9a..fA..F]>/ in Perl 6        == [0123456789abcdefABCDEF]
9. /[0-9a-fA-F]/ in all other dialects == [0123456789abcdefABCDEF]

### Exclusion

1. /<-[0..9a..fA..F]>/ in Perl 6        == [^0123456789abcdefABCDEF]
2. /[^0-9a-fA-F]/ in all other dialects == [^0123456789abcdefABCDEF]

3. /[^0-9a-fA-F]/ == /[^(0-9a-fA-F)]/ == /[^((0-9)|(a-f)|(A-F))]/

-----------------------------------------------------------------------------

## Classes

1. Each programming language comes with its own documentation for its character classes.
   - in short are a building sets of `[SET]`
   
2. for php for exampe [:xdigit:] == Hexadecimal == [0123456789abcdefABCDEF]
   - for Hexadecimal [a-f] has the same value of [A-F]
   -     Hexadecimal = Base16.
   
3. In JavaScript, character classes are escape sequences.

### Hexadecimal

### Example using IPV6

**xxxx : xxxx : yyyy : yyyy : zzzz : zzzz : wwww : wwww**

1. for each set of single x or single y or ... you have like it be a sum of : 2^0 + 2^1 + 2^2 + 2^3

2. with a base 16 == HEX you can describe 16 values in one time,
   the same thing that you can do with set these binaries : 2^0 + 2^1 + 2^2 + 2^3
   so in shor HEX has more power of description of Decimal,
   Decimal has more power of description of Binary,
   --> a*2^0 + b*2^1 + c*2^2 + d*2^3 == [:xdigit:]{1}
   
3. FOR `IPV6` == **[:xdigit:]{8} \: [:xdigit:]{8} \: [:xdigit:]{8} \: [:xdigit:]{8}**

-----------------------------------------------------------------------------
