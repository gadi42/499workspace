#!/usr/bin/env python3


def apply_amp_filter(data, cutoff=0.8):
    """
    Apply an amplitude filter to an iterable, returning a list.
    """

    # Make an empty list
    filtered = []

    # Add one element at a time to the list.  There are a lot of ways to do this; this is just one of them.
    for datum in data:
        datum = min(datum, cutoff)
        filtered.append(datum)
    
    # Return the new list
    return filtered
