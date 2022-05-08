
-----------------------------------------------------------------------------

# Exercise 1

## Which of the following strings does /^list|lost|lust$/ match in JavaScript, and why?

1. if java support ^ or $ i can say that might they have precedence , so the first three sequences
2. else                   i can say only lostlist.

3. only one is correct --> java support line match and words matches

### prove it with:

1. 'list'.match( /^list|lost|lust$/ )
   ["list", index: 0, input: "list"]
   
2. 'lostlist'.match( /^list|lost|lust$/ )
   ["lost", index: 0, input: "lostlist"]

3. 'listlist'.match( /^list|lost|lust$/ )
   ["list", index: 0, input: "listlist"]
   
4. 'lustlist'.match( /^list|lost|lust$/ )
   null
   
**The | operator has the lowest precedence, which means that both the ^ and the $ bind stronger.**


### for /^(list|lost|lust)$/

1. 'list'.match( /^(list|lost|lust)$/ )
   ["list", index: 0, input: "list"]
   
2. 'lostlist'.match( /^(list|lost|lust)$/ )
   null
   
3. 'listlist'.match( /^(list|lost|lust)$/ )
   null
   
4. 'lustlist'.match( /^(list|lost|lust)$/ )
   null

-----------------------------------------------------------------------------

# Exercise 2

**Let’s determine the capture groups in the following PCRE regular expression: /^a(b|c(d|(e))(f))$/**

```
    /^a(b|c(d|(e))(f))$/ ==
    ------------------------
    /^a(
        b|c(
            d|(e)
        )(f)
    )$/
    ------------------------
```

1. (e) => (e) != [e]
   - (^...) = negazione del group ?
   - [^...] = negazione del set   !
   
2. group keep order and doesn't accept mix
   - (abc) doesn't match 'cab' or 'ccab' that it's matched by [abc]
   
3. what is (a)(b) meaning ?
   - maybe it's like /a b/ like /casa mia/
   
4. what is a(b) meaning ?
   - maybe it's like 3.

5. or have precedence before (..) ?
   - i think yes : correct

## Solution:

```
     a in any case +
     + group b|c +
     + group d|e +
     f in any case .
   ---------------------------
```

## Notes

**In Perl 6, capture group numbering is different to PCE**

1. PCE = 1,2,3,4      , remember iteration
2. PERL = 0,00,000,01 , remember recursion

