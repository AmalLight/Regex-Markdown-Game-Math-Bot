
-----------------------------------------------------------------------------

# Assembling a regular expression matching a price label

# For They:

        ****€19.00****
        *-*€19.00*-*
        --€19.00--

**price ranges between 1.00 and 9999.99 euros**

1. /^$/ We are matching for the whole string, not just substrings.

2. /^[\*-]+$/ We start with any number of highlighter characters.

3. /^[\*-]+€\.$/ We place the euro sign and the escaped dot character in the expression.

4. /^[\*-]+€\d{1,4}\.\d{2}$/ Then we add the digits,
   making sure that there are always two digits after the decimal point.
   
## Using a backreference to match a price label

1. /^([\*-]+)€\d{1,4}\.\d{2}$/ Capture the substring that has to be repeated

2. /^([\*-]+)€\d{1,4}\.\d{2}\1$/ Access and insert the exact substring 
   matched in capture group 1 using \1
   
## ALL togheter

1. /^([\*-]+)€\d{1,4}\.\d{2}\1$/.exec( '****€19.00****' )

```
    {
        0: "****€19.00****",
        1: "****",
        index: 0,
        input: "****€19.00****"
    }

```

2. PCRE-compatible regular expression that detects four-letter palindrome 4 words.
   - `/^(.)(.)\2\1$/`
  
-----------------------------------------------------------------------------

# Capture Groups and Performance

- To avoid the performance penalty ( that create fake group ),
  it is possible to define parentheses that do not create capture groups.
  These parentheses are only there for overriding precedence.
  
- Language  No-Capture Parentheses
  EMACS    |   /(?:exp)/
  ERE,PCRE |   /(?:exp)/
  Perl 6   |   / [exp] /
  VIM      |   /\%(exp)/
  
## Extensions to Capture Groups

**Some PCRE-based languages offer even more features.**

- to find in their documentation

-----------------------------------------------------------------------------

