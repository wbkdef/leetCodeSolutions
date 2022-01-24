"""
From: https://leetcode.com/problems/interval-list-intersections/solution/
"""

from __future__ import annotations

from typing import Optional


class Solution:
    def intervalIntersection(
            self, firstList: list[list[int]], secondList: list[list[int]]
    ) -> list[list[int]]:
        i = j = 0
        intersections = []
        while i < len(firstList) and j < len(secondList):
            lower = max(firstList[i][0], secondList[j][0])
            upper = min(firstList[i][1], secondList[j][1])
            if upper >= lower:
                intersections.append([lower, upper])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return intersections


if __name__ == "__main__":
    res = Solution().intervalIntersection(
        firstList = [[0,2],[5,10],[13,23],[24,25]],
        secondList = [[1,5],[8,12],[15,24],[25,26]])
    assert res == [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

    res = Solution().intervalIntersection(
        firstList = [[1,3],[5,9]],
        secondList = [])
    assert res == []

    print(f"all done")
