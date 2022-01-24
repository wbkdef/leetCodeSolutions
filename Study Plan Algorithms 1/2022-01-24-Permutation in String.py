"""
From: https://leetcode.com/problems/01-matrix/
"""


from typing import Optional, Literal, Set
import itertools as it


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        d = {}

        def update(key, val):
            if key not in d:
                d[key] = val
            else:
                d[key] += val

            if d[key] == 0:
                d.pop(key)
        def add(key): update(key, 1)
        def sub(key): update(key, -1)

        for c in s1:
            sub(c)

        for i in range(len(s1)):
            add(s2[i])
        if not d:
            return True

        for i in range(len(s1), len(s2)):
            add(s2[i])
            sub(s2[i-len(s1)])
            if not d:
                return True

        return False


if __name__ == "__main__":
    res = Solution().checkInclusion(s1 = "ab", s2 = "eidbaooo")
    assert res == True

    res = Solution().checkInclusion(s1 = "ab", s2 = "eidboaoo")
    assert res == False

    res = Solution().checkInclusion(s1 = "ab", s2 = "a")
    assert res == False

    print(f"all done")
