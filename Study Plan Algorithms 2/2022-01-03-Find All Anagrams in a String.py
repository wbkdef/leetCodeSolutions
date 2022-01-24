"""
From: https://leetcode.com/problems/find-all-anagrams-in-a-string/solution/
"""

from typing import Iterable
import dataclasses


@dataclasses.dataclass
class Counter:
    counts: dict[str, int] = dataclasses.field(default_factory=dict)

    def add(self, s)  ->  None:
        if s in self.counts:
            self.counts[s] += 1
        else:
            self.counts[s] = 1

    def add_all(self, ss: Iterable[str])  ->  None:
        for s in ss:
            self.add(s)

    def remove(self, s):
        self.counts[s] -= 1
        assert self.counts[s] >= 0
        if self.counts[s] == 0:
            self.counts.pop(s)


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if not p:
            return list(range(len(s)))

        counts_p = Counter()
        counts_p.add_all(p)

        counts_s = Counter()
        counts_s.add_all(s[:len(p) - 1])

        anagram_inds = []
        for i in range(len(s)-len(p)+1):
            counts_s.add(s[i+len(p)-1])
            if counts_s == counts_p:
                anagram_inds.append(i)
            counts_s.remove(s[i])
        return anagram_inds

    def findAnagramsBrute(self, s: str, p: str) -> list[int]:
        if not p:
            return list(range(len(s)))
        sp = sorted(p)
        anagram_inds = []
        for i in range(len(s)-len(p)+1):
            ss = sorted(s[i:i+len(p)])
            if ss == sp:
                anagram_inds.append(i)
        return anagram_inds



if __name__ == "__main__":
    res = Solution().findAnagrams(s = "cbaebabacd", p = "abc")
    assert res == [0,6]

    res = Solution().findAnagrams(s = "abab", p = "ab")
    assert res == [0,1,2]

    res = Solution().findAnagrams(s = "", p = "ab")
    assert res == []

    res = Solution().findAnagrams(s = "abab", p = "")
    assert res == [0,1,2,3]

    print(f"all done")
