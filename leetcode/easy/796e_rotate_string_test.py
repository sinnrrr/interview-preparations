import collections


# defdefdefabc defdefabcdef
#
# defdef|d|efabc defdefabcdef i=6
# efdef|d|efabc defdefabcdef i=5
# fdef|d|efabce defdefabcdef i=4
# def|d|efabcef defdefabcdef i=3


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        q = collections.deque(s)
        n = len(s)
        i, swaps = 0, 0
        while i < n and swaps < n:
            if q[i] == goal[i]:
                i += 1
            elif q[i] != goal[i]:
                q.append(q.popleft())
                swaps += 1
        return "".join(q) == goal


def test():
    # assert Solution().rotateString("defdefdefabc", "defdefabcdef") is True
    # assert Solution().rotateString("aa", "a") is True
    assert Solution().rotateString("ohbrwzxvxe", "uornhegseo") is False
