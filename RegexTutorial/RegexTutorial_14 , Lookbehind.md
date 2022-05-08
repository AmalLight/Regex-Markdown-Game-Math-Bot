
-----------------------------------------------------------------------------

# Lookbehind Table

| Lookahead Type --- | --- PCRE Syntax ---- | Perl 6 Syntax -- |
| Positive --------- | -- (?<=pattern) ---- | <?after pattern> |
| Negative --------- | -- (?<!pattern) ---- | <!after pattern> |
| Word boundary ---- | -------- \b -------- | ------ << ------ |

## Word boundary

- search only for each single words

1. /...\b/ for Lookahead
2. /\b.../ for Lookbehind

## Example/Exercise

1. for match `list,lost or lust`:
   - /\bl[iou]st/

## Lookbehind

**(?=.c) in /b(?<=a.)c**

1. in SHORT: b , c , ab , a , bc <-- returned from search

2. input: **abc**

3. command : `b(?<=a.)c`

4. output: `bc`
