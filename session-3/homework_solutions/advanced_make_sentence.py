import random

grammar = {
    "_S": ["_NP _VP"],
    "_NP": ["_N",
            "_A _N _P _A _N"],
    "_VP": ["_V",
            "_V _NP"],
    "_N": ["developer", "teacher", "student"],
    "_A": ["smart", "interesting", "nice", "desperate", "annoying"],
    "_P": ["next to", "near"],
    "_V": ["learns", "trains", "tests", "is", "studies", "asks"]
}

def is_terminal(token):
    """
    Returns `True` unless the first character of the token is underscore.
    """
    # we can take index of strings just like lists - so here, if the first
    # character of a string is different from underscore then this function
    # returns True
    return token[0] != "_"


def expand(grammar, tokens):
    """
    Recursive function that gets a non-terminal token and replaces it with
    other tokens.
    """
    for i, token in enumerate(tokens):
        # skip over terminals
        if is_terminal(token):
            # if is_terminal(token) returns true then the for loop continues to
            # the next i, token in enumerate(tokens) instead of completing the
            # code in the loop
            continue
        # if we get here, we found a non-terminal token
        # so we need to choose a replacement at random
        # random.choice selects a random entry in a list
        replacement = random.choice(grammar[token])
        if is_terminal(replacement):
            # if the selected replacement is a proper word it just overwrites
            # the same position in the list (if the replacement was selected
            # from _N, _A, _P, or _V)
            tokens[i] = replacement
        else:
            # if we get one of the tokens that don't terminate then we make
            # more tokens and put them in place of the old token
            tokens = tokens[:i] + replacement.split() + tokens[(i + 1):]

        # now call expand on the new list of tokens
        # this is a recursive call - expand calls itself but with a modified
        # input (tokens has changed)
        return expand(grammar, tokens)

    # if we get here we had all terminals and are done
    return tokens


def generate_sentence(grammar):
    """
    Takes a grammar as an argument and initialises with the "_S" token,
    indicating the sentence token of the grammar.
    """
    return expand(grammar, ["_S"])


if __name__ == 'main':
    # string.join(iterable) makes a new string of each element of the
    # iterable, separated by whatever string is
    print(' '.join(generate_sentence(grammar)))
