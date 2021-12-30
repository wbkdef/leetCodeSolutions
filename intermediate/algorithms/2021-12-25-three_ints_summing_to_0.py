"""
From: https://leetcode.com/problems/3sum/
PC:KEYjqKL:
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ns = sorted(nums)
        res = set()

        for i in range(len(ns) - 2):
            if ns[i] + ns[i+1] + ns[i+2] > 0:
                break
            j = i+1
            k = len(ns) - 1
            while j < k:
                s = ns[i] + ns[j] + ns[k]
                if s == 0:
                    res.add((ns[i], ns[j], ns[k]))
                    if ns[k-1] == ns[k]:
                        k -= 1
                    else:
                        j += 1
                elif s > 0:
                    k -= 1
                else:
                    assert s < 0
                    j += 1
        return [list(t) for t in sorted(res)]


if __name__ == "__main__":
    res = Solution().threeSum([-1,0,1,2,-1,-4])
    assert res == [[-1,-1,2],[-1,0,1]]

    res = Solution().threeSum([])
    assert res == []

    res = Solution().threeSum([0])
    assert res == []

    print(f"All done")