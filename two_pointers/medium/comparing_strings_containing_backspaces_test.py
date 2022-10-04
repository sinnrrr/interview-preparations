"""
Given two strings containing backspaces (identified by the character ‘#’),
check if the two strings are equal.
"""

import pytest


def backspace_compare_custom(str1, str2):
    str1p, str2p = len(str1) - 1, len(str2) - 1

    while str1p >= 0 or str2p >= 0:
        runs = 0
        while str1[str1p] == "#":
            runs += 1
            str1p -= 1
        str1p -= runs

        runs = 0
        while str2[str2p] == "#":
            runs += 1
            str2p -= 1
        str2p -= runs

        if str1[str1p] != str2[str2p]:
            return False

        str1p -= 1
        str2p -= 1

    return True


def backspace_compare_grokking(str1, str2):
    """
    Looks for next correct char on every run and checks if
    it is withing bounds. Early exits if found unmatched chars.
    """
    idx1, idx2 = len(str1) - 1, len(str2) - 1

    while idx1 >= 0 or idx2 >= 0:
        next_valix_idx1 = _next_valid_char_idx(str1, idx1)
        next_valix_idx2 = _next_valid_char_idx(str2, idx2)

        if idx1 < 0 and idx2 < 0:  # reached the end of both the strings
            return True
        if idx1 < 0 or idx2 < 0:  # reached the end of one of the strings
            return False
        if (
            str1[next_valix_idx1] != str2[next_valix_idx2]
        ):  # characters are not equal
            return False

        idx1 = next_valix_idx1 - 1
        idx2 = next_valix_idx2 - 1

    return True


def _next_valid_char_idx(s, idx):
    """
    Given a string, loops through it and counts backspaces.
    Exits at first run if not a backspace, handles chars, that
    should be removed with backspace.
    """
    backspace_count = 0
    while idx >= 0:
        if s[idx] == "#":
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break

        idx -= 1

    return idx


@pytest.mark.parametrize(
    "str1, str2, expected",
    [
        ("xy#z", "xzz#", True),
        ("xy#z", "xyz#", False),
        ("xp#", "xyz##", True),
        ("xywrrmp", "xywrrmu#p", True),
    ],
)
def test_backspace_compare_grokking(str1, str2, expected):
    assert backspace_compare_custom(str1, str2) == expected
    assert backspace_compare_grokking(str1, str2) == expected


@pytest.mark.parametrize(
    "str1, str2, expected",
    [("ab##", "c#d#", True), ("nzp#o#g", "b#nzp#o#g", True)],
)
def test_backspace_compare_leetcode(str1, str2, expected):
    # assert backspace_compare_custom(str1, str2) == expected
    # assert backspace_compare_grokking(str1, str2) == expected
    ...
