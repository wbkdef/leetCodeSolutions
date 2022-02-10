"""
From: https://leetcode.com/problems/gray-code/
"""


class Solution:
    def grayCode(self, n: int) -> list[int]:
        assert n >= 0
        if n == 0:
            return [0]

        gcm1 = self.grayCode(n-1)
        gc = gcm1[:]
        for c in reversed(gcm1):
            gc.append(c ^ (1 << (n-1)))

        return gc


if __name__ == "__main__":
    assert Solution().grayCode(0) == [0]
    assert Solution().grayCode(1) == [0, 1]
    assert Solution().grayCode(2) == [0, 1, 3, 2]
    assert Solution().grayCode(3) == [0, 1, 3, 2, 6, 7, 5, 4]

    print(f"all done")
