class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 0
        res = ""

        for i in range(n):
            lp = rp = i
            while lp >= 0 and rp < n and s[lp] == s[rp]:
                new_len = rp - lp + 1
                if new_len > max_len:
                    res = s[lp : rp + 1]
                    max_len = new_len
                lp -= 1
                rp += 1

            lp, rp = i, i + 1
            while lp >= 0 and rp < n and s[lp] == s[rp]:
                new_len = rp - lp + 1
                if new_len > max_len:
                    res = s[lp : rp + 1]
                    max_len = new_len
                lp -= 1
                rp += 1

        return res


def test():
    assert Solution().longestPalindrome("babad") == "bab"
