def flatten(seq):
    for el in seq:
        if isinstance(el, list):
            yield from flatten(el)
        else:
            yield el

    