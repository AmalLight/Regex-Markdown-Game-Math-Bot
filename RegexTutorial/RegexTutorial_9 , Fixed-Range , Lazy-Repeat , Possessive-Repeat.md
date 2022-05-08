
-----------------------------------------------------------------------------

# Fixed-Range  Matching

**Remember on 8 we talk about (+,?,*)**

## Dialect and Notation

- BRE, EMACS -- /a\{2,5\}/
- ViM -- /a\{2,5}/
- ERE , PCRE -- /a{2,5}/
- PERL 6 -- / a ** 2..5 /

### Matching at least two a characters

## Dialect Notation

- BRE, EMACS -- /a\{2,\}/
- VIM -- /a\{2,}/
- ERE , PCRE -- /a{2,}/
- PERL 6 -- / a ** 2..* /

### Loop  Exactly n Times

## Dialect Notation

- BRE, EMACS -- /a\{2\}/
- VIM -- /a\{2}/
- ERE , PCRE -- /a{2}/
- PERL 6 -- / a ** 2 /

**b{,3} not work , is an error**

-----------------------------------------------------------------------------

# Lazy Repeat Modifiers

**(..)?** , **?**

1. a*? matches zero or more a characters and attempts to match as few a characters as possible.
   - few a characters as possible => OPTIONAL LEFT.
   - (¿.+)?(\?) = it's different from XOR because =>
     if match LEFT return matches for LEFT|RIGHT
     else          return matches for RIGHT
   
2. a+? matches one or more a characters and attempts to match as few a characters as possible.
   - few a characters as possible ...
   
3. a?? matches zero or one a characters, first attempting not to match the a character.
   - what_is_meaning_? ...
   
4. a{1,2}? attempts to match the a character once or twice, first trying to match it once.
   - **In Perl 6, the equivalent syntax is a **? 1..2.**

5. **¿[^\?]+\?** , genius : match any character except `\?`

-----------------------------------------------------------------------------

# Possessive Repeat Modifiers

## yielding a*+, a++, a?+, a{1,2}+ loops.

### Possessive repeat modifiers are available in PCRE and in Perl 6.

### Some languages like JavaScript don’t have possessive repeat modifiers

#### In Perl 6, we write a : after the repeat modifier: a*:, a+:, a?:, a **: 1..2.

1. (?=(a+))\1 is equivalent to a++

2. Consequence more **Complex and NOT Useful**


