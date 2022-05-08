
# H1

## H2

_where H1 > H2 , written on italics_

### H ? 3

# Tutorial

## Paragraphs

To create paragraphs,
use a blank line to separate one or more lines of text.
You should not indent paragraphs with spaces or tabs:

p1

p2

..

pn

To create a line break (<br>),
end a line with two or more spaces, and then type return:

p1 start , break
continue here .. end


## Emphasis on text

blood : **bold text** ; __bold text__ ; no blood **is blood** no blood .

italic : no ita *is ita* ; no ita _is ita_ ; no ita *is ita* no ita .

mix blood and italic :
    ***Important*** no mixed .
    ___Important___ no mixed .
    no mixed __*Important*__ no mixed .
    no mixed **_Important_** no mixed .


## Blockquote on pharagraph

To create a blockquote, add a > in front of a paragraph :

> p1 , this is a blockquote for all p1 pharagraph

Blockquotes with Multiple Paragraphs :
  Blockquotes can contain multiple paragraphs.
  Add a > on the blank lines betweenthe paragraphs :
    > p1
    >
    > p2


## Elements

Blockquotes can contain other Markdown formatted elements.
Not all elements canbe used — you’ll need to experiment to see which ones work

test:
- el1
- el2
- el3


## List

### Ordered Lists

1. First item  -> 1. First item
2. Second item -> 2. Second item
3. Third item  -> 3. Third item
4. Fourth item -> 4. Fourth item

1. First item  -> 5. First item
1. Second item -> 6. Second item
1. Third item  -> 7. Third item
1. Fourth item -> 8. Fourth item

1. First item  -> 9.  First item
8. Second item -> 10. Second item
3. Third item  -> 11. Third item
5. Fourth item -> 12. Fourth item

a. First item  -> a. First item  = doesn't work

b. Second item -> b. Second item = doesn't work

### Nesting List Items = +4 tab

1. First item
2. Second item
3. Third item
    1. Indented item
    2. Indented item
4. Fourth item

- First item
- Second item
- Third item
    - Indented item
    - Indented item
- Fourth item

### Unordered Lists

- First item
- Second item
- Third item
- Fourth item

* First item
* Second item
* Third item
* Fourth item

+ First item  = type different of a list
* Second item = type different of a list
- Third item  = type different of a list
+ Fourth item = type different of a list

## Code as text = +8 tab

1.  Open the file.
2.  Find the following code block on line :

        <html>
            <head>
                <title>Test</title>
            </head>
        </html>

3.  Update the title to match the name of your website
4.  At the command prompt, type `nano` .

5. Escaping Tick Marks : ``Use `code` in your Markdown file.``

```
{
    "firstName": "John1",
    "lastName": "Smith1",
    "age": 11
}
```

```json
{
    "firstName": "John2",
    "lastName": "Smith2",
    "age": 22
}
```

~~~
{
    "firstName": "John3",
    "lastName": "Smith3",
    "age": 33
}
~~~

## Images = +4 tab

1.  Open the file containing Tux, the Linux mascot.
2.  Marvel at its beauty.

    ![Tux](images/tux.png)

3.  Close the file.

4.  ![Philadelphia's Magic Gardens. This place was so cool!](images/philly-magic-garden.png "Philadelphia's Magic Gardens")

## Horizontal Rules

1. ***
2. ---
3. _________________

--------------------

## Links

1. Use [Duck Duck Go](https://duckduckgo.com).

2. Adding Titles : [Duck Duck Go](https://duckduckgo.com "My search engine!") (on hover with mouse) .

3. urls and email on clear : <https://eff.org>
4. urls and email on clear : <fake@example.com>

5. **strong** can be used on urls/links

6. link inside the text : [Heading IDs](#heading-ids)

7. Disabling Automatic URL Linking : `http://www.example.com`


## Escaping Characters

\* Symbol used without create a unordered list.


## Table

-----------------------------
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

-----------------------------

| Syntax | Description |
| --- | ----------- |
| Header | Title |
| Paragraph | Text |

-----------------------------

| Syntax     | Center          | Right            |
| :---       |        :----:   |             ---: |
| Header     | Title           | Here's this      |
| Paragraph  | Text            | And more         |

-----------------------------

## Notes

Here's a simple footnote,[^1] and here's a longer one.[^bignote]

[^1]: This is the first footnote.

[^bignote]: Here's one with multiple paragraphs and code.

    Indent paragraphs to include them in the footnote.

    `{ my code }`

    Add as many paragraphs as you like.

## ID

1. create link:

    #### My Great Heading {#custom-id}

1. link inside the text : [Heading IDs](#heading-ids)

## Strike

You can “strikethrough” words by putting a horizontal line through the center:

1. The world is ~~flat~~ round.

#Task Lists

1.

     [x] Write the press release
     [ ] Update the website
     [ ] Contact the media
2.

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

---

# NOT IMPORTANT

## Definition Lists

First Term
: This is the definition of the first term.

Second Term
: This is one definition of the second term.
: This is another definition of the second term.
