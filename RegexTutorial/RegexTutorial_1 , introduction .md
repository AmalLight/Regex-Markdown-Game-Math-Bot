
-----------------------------------------------------------------------------

# Language used

## javascript

1. invoking 1: obj.match ( ... )
   - obj is a java's string object
   - ... is a regular expression
   - it returns an array of matches

2. ivoking 2: /.../.test( obj )
   - it returns ( true if ... match least one time on obj , else false )
   
3. starting : const regex = new RegExp( 're' );

## Python3

1. starting : regex = re.compile( r"xy+" )

-----------------------------------------------------------------------------
   
# Explain how it's Hard to Use

1. Hard to understand
2. Hard to write
3. Hard to modify
4. Hard to test
5. Hard to debug

-----------------------------------------------------------------------------

# Example of coding regex

## Coding for Bre,  ere,  eMaCs, VIM, pCre , Perl

1. BRE, ERE, EMACs, VIM, PCRE
2. BRE
3. ERE, PCRE, PERL
4. PERL

1. [^0123456789] for (1)
   - [  ... ] match any characters in this set
   - [ ^... ] ^ is negation for this set, so match any characters that they aren't in this set

2. <-[0123456789]> for PERL
   - [  ... ] match any characters in this set
   - [ ^... ] ^ is negation for this set, so match any characters that they aren't in this set
   
### OR

1. BRE : or operator is not supported
2. ERE,PCRE,PERL : /0|1|2/
3. EMACS,VIM :   /0\|1\|2/

4. An equivalent BRE expression would be /[012]/,
   using a character set.

## literal characters

1. YES they are   : **, !, %, =, _**
1. NO they aren't : **., *, ^, $, [, ]**

-----------------------------------------------------------------------------

