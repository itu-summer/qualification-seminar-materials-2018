# Assignment for Session 8

## Write a Syntax Checker

Write a command-line program `paren_checker.py`, which can check that parentheses in a Python program are balanced.

Consider the program `my_erroneous_prg.py` in the `homework` directory. It contains a small Python program with an error. When running it with the following command it produces a syntax error, which you likely know from some of your earlier programs.

```bash
$ python my_erroneous_prg.py
  File "my_erroneous_prg.py", line 3

                   ^
SyntaxError: unexpected EOF while parsing
```

In essence, this error tells you that there is a closing parenthesis missing.


Write your command-line program `paren_checker.py` so that it receives a path to another Python program -the one to check- as a command-line argument. That is, you can call it as in the following:

```bash
$ python paren_checker.py my_erroneous_prg.py
```

Your program should produce a message like `I think all parenthesis are balanced.` in case of a correct program and another message like `Looks like you forgot to close some parenthesis...` in case of a missing parenthesis.

## Let the Syntax Checker Find All Parentheses Errors


Make sure that your program produces the correct reply also when fed with the program `my_erroneous_prg2.py`, i.e., the following should say something like `You have are closing a parenthesis without opening one`, find `my_erroneous_prg2.py` in the `homework` directory.


```bash
$ python paren_checker.py my_erroneous_prg2.py
```

## Extend the Syntax Checker

Extend your program `paren_checker.py` so that it tells the user something about on which line and on which position in the line a parenthesis is missing. That is, running it on `my_erroneous_prg2.py` could produce the following output.

```bash
$ python paren_checker.py my_erroneous_prg2.py
You have are closing a parenthesis without opening one on line 1 on position 16
```


## Extend the Syntax Checker Even Further


Extend your program `paren_checker.py` so that it checks for all types of parentheses which can appear in Python program. These are `(`, `)`, `[`, `]`, `{`, and `}`.