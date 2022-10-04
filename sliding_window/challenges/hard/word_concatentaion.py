"""
Given a string and a list of words, find all the starting indices of
substrings in the given string that are a concatenation of all the
given words exactly once without any overlapping of words.
It is given that all words are of the same length.
"""

from collections import defaultdict

import pytest

# word_len = len(words[0])
# words_freq = dict.fromkeys(words, 0)
# matched = 0

# while i := 0 < len(str1):
#     word = str1[i - word_len:i]

#     if word in words_freq:
#         words_freq[word] -= 1
#         if words_freq[word] == 0:
#             matched += 1
#     else:
#

#     i += word_len


def find_word_concatenation(str1, words):
    words_freq = {}

    for word in words:
        if word not in words_freq:
            words_freq[word] = 0
        words_freq[word] += 1

    result_indices = []
    word_len = len(words[0])
    words_count = len(words)

    # +1 because of range()
    for i in range((len(str1) - word_len * words_count) + 1):
        words_seen = {}
        for j in range(0, words_count):
            next_word_index = i + j * word_len
            word = str1[next_word_index:next_word_index + word_len]

            if word not in words_freq:
                break

            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            if words_seen[word] > words_freq.get(word, 0):
                break

            if j + 1 == words_count:
                result_indices.append(i)

    return result_indices


def find_word_concatenation_2(str1, words):
    ans = []
    words_freq = {}
    for word in words:
        if word not in words_freq:
            words_freq[word] = 1
        else:
            words_freq[word] += 1

    word_size = len(words[0])
    window_size = word_size * len(words)
    window_start = 0
    window_end = window_size

    while window_end <= len(str1):
        substring = str1[window_start:window_end]
        for i in range(len(words)):
            w = substring[i * word_size:(i + 1) * word_size]
            if w not in words_freq:
                break
            words_freq[w] -= 1
            if words_freq[w] == 0:
                del words_freq[w]
        if not words_freq:
            ans.append(window_start)
        window_start += 1
        window_end += 1
        for word in words:
            if word not in words_freq:
                words_freq[word] = 1
            else:
                words_freq[word] += 1

    return ans


@pytest.mark.parametrize(
    "str1, words, expected",
    [
        ("catcatfoxfox", ["cat", "fox"], [3]),
        ("catfoxcat", ["cat", "fox"], [0, 3]),
    ],
)
def test_find_word_concatenation(str1, words, expected):
    assert find_word_concatenation(str1, words) == expected
    # assert find_word_concatenation_2(str1, words) == expected
