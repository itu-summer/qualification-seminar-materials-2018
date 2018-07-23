# Ice Cream Challenge

![](https://vignette.wikia.nocookie.net/spongebob/images/8/80/Sb2_ice_cream_kisses.gif/revision/latest?cb=20160518181528)

Write a program with an algorithm that tells you if a word is contained in a text file.

That is, you would like to wrap that in a function `is_in`, which takes the word to find as first argument and the text as second argument, see the following:


```python
def is_in(word, text):
    # TODO: Implement me!
    pass
```


Your program may not use the Python inbuilt `in` functionality. That is, you cannot just do something like this:

```python
text = '''"I think not, Holmes.  It is very warm."

"Good old Watson!  You are the one fixed point in a changing age.
There's an east wind coming all the same, such a wind as never blew on
England yet.  It will be cold and bitter, Watson, and a good many of us
may wither before its blast.  But it's God's own wind none the less,
and a cleaner, better, stronger land will lie in the sunshine when the
storm has cleared.  Start her up, Watson, for it's time that we were on
our way.  I have a check for five hundred pounds which should be cashed
early, for the drawer is quite capable of stopping it if he can."'''

def is_in(word, text):
    return 'bitter' in text
```

Additionally, you shall not solve it like this:

```python
text = '''"I think not, Holmes.  It is very warm."

"Good old Watson!  You are the one fixed point in a changing age.
There's an east wind coming all the same, such a wind as never blew on
England yet.  It will be cold and bitter, Watson, and a good many of us
may wither before its blast.  But it's God's own wind none the less,
and a cleaner, better, stronger land will lie in the sunshine when the
storm has cleared.  Start her up, Watson, for it's time that we were on
our way.  I have a check for five hundred pounds which should be cashed
early, for the drawer is quite capable of stopping it if he can."'''

def is_in(word, text):
    for w in text.split():
        if word == w:
            return True
```

Instead make use of some of the `find_*` algorithms, which we discussed today in class.

The person that hands-in the fastest algorithm together with a correct runtime analysis will get two balls of ice cream from Ismejeriet, the ice cream shop opposite ITU.

Make use of the Sherlock Holmes stories in this dictionary.
