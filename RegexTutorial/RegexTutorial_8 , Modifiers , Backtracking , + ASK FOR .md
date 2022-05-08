
-----------------------------------------------------------------------------

# Repeat Modifiers

1. + Match at least once
   - from 1 to any number > 1

2. ? Match at most once
   - also zero is ok
   - max is one to pass over
   - After pass , max is infinity for merge over

3. * Match any number of times
   - also zero is ok , is accepted
   - max is infinity

4. {min,max} Match at least min times, and at most max times
   - {X,Y} == ( math --> [X,Y] )

5. {n} Match exactly n times
   - {n} == ( math --> [n,n] )

-----------------------------------------------------------------------------

# Backtracking

1. ab+ matches an a and then at least one b.
   Matching strings are ab, abb, abbb, and so on.
   
2. [ab]+ matches any number of a or b character in any order,
   assuming the matched sequence is at least one character long.
   Matching strings are a, b, aa, ab, ba, bb, aaa, aab, and so on.
   
3. (ab)+ matches at least one ab sequence. Matching strings are ab, abab, ababab, and so on.

-----------------------------------------------------------------------------

# Match at Least Once

1. a+ to denote matching the a character at least once
   - at least once

2. [ab]+ to denote matching the a or the b character at least once

3. (ab)+ to denote matching the ab sequence at least once

4. [ab]+ == [a|b]+ == (a|b)+

-----------------------------------------------------------------------------

# Dialet and Notation for the At Least Once Loop

- BRE                 -- None; use aa*
- ERE, PCRE, PERL 6   -- a+
- EMACS, VIM          -- a\+

-----------------------------------------------------------------------------

# Match at Most Once: Optionals

1. a? to denote matching the a character at most once
   - at most once

2. [ab]? to denote matching the a or the b character at most once

3. (ab)? to denote matching the ab sequence at most once

-----------------------------------------------------------------------------

# Match Any Number of Times

1. a* denotes matching any number of a characters.
   - any number of a characters =>
   - at least once
   - at most once
   - --> at least once | at most once
   
2. [ab]* denotes matching the a or b character any number of times.

3. (ab)* denotes matching the ab sequence any number of times.

**Don’t forget to escape the parentheses with \( and \) in EMACS and VIM**

