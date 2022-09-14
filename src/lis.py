"""Computing increasing substrings."""

# The Any annotations here is saying that we will accept any .
# They *should* be comparable, and it *is* possible to make such
# an annotation, but it is tricky, and I don't want to confuse you
# more than strictly necessary.
from typing import Sequence, Any


def is_increasing(x): #Sequence[Any]) -> bool:
    """
    Determine if x is an increasing sequence.

    >>> is_increasing([])
    True
    >>> is_increasing([42])
    True
    >>> is_increasing([1, 4, 6])
    True
    >>> is_increasing("abc")
    True
    >>> is_increasing("cba")
    False
    """
    for i in range(len(x) - 1):
        if not x[i] < x[i+1]:
            return False
    return True


def substring_length(substring): #tuple[int, int]) -> int:
    """Give us the length of a substring, represented as a pair."""
    return substring[1] - substring[0]


def longest_increasing_substring(x): #Sequence[Any]) -> tuple[int, int]:
    """
    Locate the (leftmost) longest increasing substring.

    If x[i:j] is the longest increasing substring, then return the pair (i,j).

    >>> longest_increasing_substring('abcabc')
    (0, 3)
    >>> longest_increasing_substring('ababc')
    (2, 5)
    >>> longest_increasing_substring([12, 45, 32, 65, 78, 23, 35, 45, 57])
    (5, 9)
    """
    # The leftmost empty string is our first best bet
    best = (0, 0)
    i,j=0,1
    while j <= len(x):
        if is_increasing == True:
            if substring_length((i,j))>substring_length(best):
                best(i,j)
                j+=1
            else:
                j+=1
        else:
            i +=1
            j=1+1
    return best

print(longest_increasing_substring('abcabc'))
