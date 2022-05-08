
-----------------------------------------------------------------------------

# Finite State Machines

1. After reading the first a character,
   we move the token through the arrow denoted by the a state.
   The token is now in the intermediate state.
   
2. After reading the second a, there is no arrow starting in the intermediate state;
   therefore, we move back to the start state. In this state, we try reading a again.
   As there is an a arrow originating from the start state,
   we move to the intermediate state again.
   
3. After reading the b character, we move our token from the intermediate state to the match state.
   Given that we have reached the match state, the string matches the regular expression.

# Backtracking, remember Prolog.

# Deterministic XOR and Non-Dterministic (OR=a|b) -- Regex Modeling

**[] , () , a|b** =>
  - [] = SET
  - () = PRIORITY
  - I HAVE to search for XOR , visualizing as {a|b} but {a,b} meaning range loop
    find : `/^(a|b){1}$/`
  - a|b = a,b OR

**A Successful Match Is Cheaper Than Failure**

-----------------------------------------------------------------------------

# Simplifiers == Equivalences

for each replica of (list+lost+lust):

    given Rule : (ab+ac) == a(b+c)
     result is : l(ist+ost)+ust
     
    given Rule : (ab+ac) == a(b+c)
     result is : l((ist+ost)+ust)
     
    given Rule : (ab+cb) == (a+c)
     result is : l(((is+os)t)+ust)
     
    given Rule : (a) == a
     result is : l((is+os)t+ust)
     
    given Rule : (ab+cb) == (a+c)b
     result is : l(((is+os)+us)t)
     
    given Rule : (ab+cb) == (a+c)b
     result is : l((((i+o)s)+us)t)
     
    given Rule (a) == a
     result is : l(((i+o)s+us)t)
     
    given Rule (ab+cb) == (a+c)b
     result is : l((((i+o)+u)s)t)
     
    given Rule : ab(cd) == abcd
     result is : l(((i+o)+u)s)t
     
    given Rule : ab(cd) == abcd
     result is : l((i+o)+u)st
     
    given Rule : (a+(b+c)) == a+b+c
     result is : l(i+o+u)st

