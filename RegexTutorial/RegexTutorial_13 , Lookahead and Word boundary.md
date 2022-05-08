
-----------------------------------------------------------------------------

# Lookahead Table

| Lookahead Type --- | --- PCRE Syntax --- | Perl 6 Syntax --- |
| Positive --------- | -- (?=pattern) ---- | <?before pattern> |
| Negative --------- | -- (?!pattern) ---- | <!before pattern> |
| Word boundary ---- | ------- \b -------- | ------ >> ------- |

## Word boundary

- search only for each single words

## Example/Exercise

1. for match `list,lost or lust`:
   - /l[iou]st\b/

## Lookahead

**(?=.c) in /a(?=.c)b**

- it will be more correctly to write:
  `a(?=.)b` with . as c.

1. First we read a.

2. Then we enter the lookahead, memorizing the index
   1 pointing at character b of abc.
   
3. We match the character b as an arbitrary character
   inside the lookahead.

4. We match the character c in the lookahead.

5. As the lookahead succeeds, we exit from the
   lookahead construct with success and revert to
   position 1 in the string.
   
6. We match character b in the string.

7. The regex matching succeeds, and the substring
   "ab" starting at position 0 is returned. Word
   boundaries work like a positive lookahead.

8. in SHORT: a , b , bc , c , ab <-- returned from search

## Example/Exercise

`Suppose the following championship classification is given`
`in the form of a JavaScript template literal:`

1. for match : `1st D.Okada (5) 97Pts`
   - look : /\d+(?=Pts)/
   - note: without b.
   - result: will return only a.

-----------------------------------------------------------------------------

