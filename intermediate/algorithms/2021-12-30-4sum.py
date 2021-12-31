"""
From: https://leetcode.com/problems/4sum/
PC:KEYuQVa:
"""
import collections
import itertools

class Solution:
    def remove_5th_and_greater_copies(self, nums: list[int]) -> list[int]:
        """ Remove duplicates to make more efficient...

        This is an O(nlog(n)) cost, which may reduce the n in the later O(n**2)
        algorithm.
        """
        if len(nums) <= 4:
            return nums

        ns = sorted(nums)
        i = 4
        while i < len(ns):
            if len(set(ns[i-4:i+1])) == 1:
                ns.pop(i)
            else:
                i += 1

        print(f"Array len cut from {len(nums)} to {len(ns)}")
        return ns


    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # d2 is a mapping from sums of two values to the 2 indices that gave
        # that sum
        nums = self.remove_5th_and_greater_copies(nums)

        d2: dict[int, list[frozenset[int]]] = collections.defaultdict(list)

        for i, j in itertools.combinations(range(len(nums)), 2):
            sum2 = nums[i] + nums[j]
            d2[sum2].append(frozenset([i, j]))

        # inds_to_vals = {}
        vals = set()
        for sum2 in d2:
            if target - sum2 in d2:
                for inds12 in d2[sum2]:
                    for inds34 in d2[target - sum2]:

                        # inds4 = d2[sum2] | d2[target - sum2]
                        inds4 = inds12 | inds34
                        if len(inds4) == 4:
                            vals.add(tuple(sorted(nums[i] for i in inds4)))
                            # vals = sorted(nums[i] for i in inds4)
                            # inds_to_vals[inds4] = (sorted(inds4))

        res = sorted(list(v4) for v4 in vals)
        return res


if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    res = Solution().fourSum(nums, target)
    assert res == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

    nums = [2,2,2,2,2]
    target = 8
    res = Solution().fourSum(nums, target)
    assert res == [[2,2,2,2]]

    nums = [2,2,2,2,2]
    target = 7
    res = Solution().fourSum(nums, target)
    assert res == []

    nums = [5, 2,2,2,2,2, 2, 2, 6, 6, 6, 6, 3]
    target = 7
    res = Solution().fourSum(nums, target)
    assert res == []

    print(f"all done")
