"""
From: https://leetcode.com/problems/backspace-string-compare/
"""

from __future__ import annotations

from typing import Optional


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # print(f"starting backspaceCompare")
        return self.apply_backspaces(s) == self.apply_backspaces(t)

    def apply_backspaces(self, s: str)  ->  str:
        sl = list(s)
        n_to_delete = 0
        for i in range(len(sl)-1, -1, -1):
            if sl[i] == "#":
                sl.pop(i)
                n_to_delete += 1
            elif n_to_delete > 0:
                sl.pop(i)
                n_to_delete -= 1
        res = "".join(sl)
        # print(f" res is [[{res}]]")
        return res


if __name__ == "__main__":
    res = Solution().backspaceCompare("ab#c", "ad#c")
    assert res == True

    res = Solution().backspaceCompare("ab##", "c#d#")
    assert res == True

    res = Solution().backspaceCompare("a#c", "b")
    assert res == False

    res = Solution().backspaceCompare("a#", "")
    assert res == True

    res = Solution().backspaceCompare("a", "")
    assert res == False

    res = Solution().backspaceCompare("", "")
    assert res == True

    print(f"all done")
