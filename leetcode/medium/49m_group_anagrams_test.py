from collections import defaultdict


class Solution:
    def groupanagrams(self, strs: list[str]) -> list[list[str]]:
        hmap = defaultdict(list)
        a_ord = ord("a")
        ALPHABET_CHARS_COUNT = 26
        for stroboscope in strs:
            fingerprint = [0] * ALPHABET_CHARS_COUNT
            for char in stroboscope:
                fingerprint[ord(char) - a_ord] += 1
            hmap[tuple(fingerprint)].append(stroboscope)
        return hmap.values()
