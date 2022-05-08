
-----------------------------------------------------------------------------

# Meta Character

## for ALL

1. **.** Arbitrary character ( for any chars )
   - PERL , BRE , ERE => represents any character, including the newline.
   - PCRE , EMACS , VIM => represents any character, except the newline.
     include the newline character together with the arbitrary character class = [.\n]

2. ++*++ iterartion , match any number of times
3. **^** Two semantics: (1) negation, (2) anchor matching the start of the string or line
4. **$** Anchor matching the end of the string or line
5. **[]** set

## PCRE Meta Characters

6. **|** or
7. **?** Optional parts in the expression
8. **+** Match at least once

9. **{}** Specify a range for the number of times an expression has to match the string
10. **()** (1) grouping characters, (2) extracting substrings

## In VIM and EMACS, you have to escape the characters |, ?, {, },  (, and ) to use them as operators.

-----------------------------------------------------------------------------

# ignoring whitespaces

1. in one row : 
        /first second third/

2. in more lines :
        /
           first
           second
           third
        /

-----------------------------------------------------------------------------

# Operator Precedence and Parentheses

## Interesting Equivalences

**You can use parentheses to group expressions with lower precedence**

1. /list|lost|lust/ == /l(i|o|u)st/
  - Don’t forget to escape the parentheses in VIM and EMACS.

## Anchored Start and End

**using ^ or $**

1. for BRE, ERE, PCRE, PERL
   - /^x/ matches strings that start with x.
   - /x$/ matches strings that end with x.
   - /^x$/ matches the string 'x' with no other characters present.

2. for PCRE-based
   - /^x/ matches lines that start with x.
   - /x$/ matches lines that end with x.
   - /\Ax/ matches strings that start with x.
   - /x\z/ matches strings that end with x.

   - \A == ^
   - \z == \Z == $
   
3. for JavaScript
   - \b.. matches words starting with x.
   - ..\b matches words ending   with x.
   
   - \b... == ^
   - ...\b == $

4. for EMACS
   - /\`x/ matches strings that start with x.
   - /^x/ matches lines that start with x.
   - /x\'/ matches strings that end with x.
   - /x$/ matches lines that end with x.
   
5. for VIM
   - /\%^x/ matches strings that start with `x`.
   - /^x/ matches lines that start with `x`.
   - /x\%$/ matches strings that end with `x`.
   - /x$/ matches lines that end with `x`.
   
6. for Perl
   - `/^x/` matches strings that start with `x`.
   - `/x$/` matches strings that end with `x`.
   - `/^^x/` matches lines that start with `x`.
   - `/x$$/` matches lines that end with `x`.

**remember that \ advises you for next special char after \ , so the next will be a not literal char**

-----------------------------------------------------------------------------

