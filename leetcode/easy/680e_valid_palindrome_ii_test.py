class Solution:
    def validPalindromeWrong(self, s: str) -> bool:
        mistakes = 1
        lp, rp = 0, len(s) - 1

        while lp <= rp:
            if mistakes < 0:
                return False

            if s[lp] != s[rp]:
                mistakes -= 1

            lp += 1
            rp -= 1

        return True

    def validPalindrome(self, s: str) -> bool:
        lp, rp = 0, len(s) - 1

        while lp < rp:
            if s[lp] != s[rp]:
                if s[lp + 1 : rp + 1] == s[lp + 1 : rp + 1][::-1]:
                    return True
                if s[lp:rp] == s[lp:rp][::-1]:
                    return True
                return False
            lp += 1
            rp -= 1
        return True


def test():
    assert Solution().validPalindrome("abca") is True
