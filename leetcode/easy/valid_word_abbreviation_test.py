def solution(word: str, abbr: str):
    n1, n2, p1, p2 = len(word), len(abbr), 0, 0

    while p1 < n1 and p2 < n2:
        if word[p1] == abbr[p2]:
            p1 += 1
            p2 += 1
            continue

        if not abbr[p2].isnumeric():
            return False

        if abbr[p2] == "0" and word[p1] != abbr[p2 + 1]:
            return False

        num = ""
        while p2 < n2 and abbr[p2].isnumeric():
            num += abbr[p2]
            p2 += 1
        num = int(num)
        p1 += num

    return p1 == n1 and p2 == n2


def test():
    assert solution("internationalization", "i12iz4n") is True
    assert solution("a", "1") is True
    assert solution("a", "01") is False
    assert solution("aa", "a2") is False
