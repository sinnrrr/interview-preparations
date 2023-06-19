import pytest


class FailedSolution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        max = ""
        curr = ""
        for char in s:
            if char not in curr:
                curr += char
                if len(curr) > len(max):
                    max = curr
                continue

            curr = char
            if len(curr) > len(max):
                max = curr

        return len(max)


class SlidingWindowSolution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end, result = 0, 0, 0
        map = {}
        n = len(s)

        while end != n:
            if s[end] in map:
                result = max(result, end - start)
                duplicate_idx = map[s[end]]
                for i in range(start, duplicate_idx):
                    del map[s[i]]

                start = duplicate_idx + 1

            map[s[end]] = end
            end += 1

        return max(result, n - start)

    # window_start = 0
    # max_size = 0
    # char_index_map = {}

    # for window_end in range(len(string)):
    #     char = string[window_end]
    #     if char in char_index_map:
    #         window_start = max(window_start, char_index_map[char] + 1)

    #     char_index_map[char] = window_end
    #     max_size = max(max_size, window_end - window_start + 1)
    # return max_size


Solution = SlidingWindowSolution


@pytest.mark.parametrize(
    "str,expected",
    [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), (" ", 1), ("au", 2)],
)
def test_solution(str, expected):
    assert Solution().lengthOfLongestSubstring(str) == expected
