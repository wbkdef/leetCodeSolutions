"""
From: https://leetcode.com/problems/count-and-say/
PC:KEYqisG:
"""

import itertools as it


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        assert n > 1

        return "".join(f"{len(list(g))}{i}"
                       for i, g in it.groupby(self.countAndSay(n-1)))


if __name__ == "__main__":
    assert Solution().countAndSay(1) == "1"
    assert Solution().countAndSay(2) == "11"
    assert Solution().countAndSay(3) == "21"
    assert Solution().countAndSay(4) == "1211"
    assert Solution().countAndSay(5) == "111221"
    assert Solution().countAndSay(6) == "312211"

    print(f"all done")
