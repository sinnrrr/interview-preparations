class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permutation_set = {}
        for char in s1:
            if char not in permutation_set:
                permutation_set[char] = 0
            permutation_set[char] += 1

        start, end = 0, 0
        chars_matched = len(permutation_set.keys())
        while end < len(s2):
            if s2[end] not in permutation_set:
                end += 1
                while start != end:
                    if s2[start] in permutation_set:
                        if permutation_set[s2[start]] == 0:
                            chars_matched += 1
                        permutation_set[s2[start]] += 1
                    start += 1
                continue

            permutation_set[s2[end]] -= 1
            if permutation_set[s2[end]] == 0:
                chars_matched -= 1

            while permutation_set[s2[end]] < 0:
                if s2[start] in permutation_set:
                    if permutation_set[s2[start]] == 0:
                        chars_matched += 1
                    permutation_set[s2[start]] += 1
                start += 1

            if chars_matched == 0:
                return True

            end += 1

        return False


def test():
    assert Solution().checkInclusion("ab", "eidbaooo") is True
    assert Solution().checkInclusion("ab", "eidboaoo") is False
    assert Solution().checkInclusion("adc", "dcda") is True
