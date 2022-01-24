"""
From: https://leetcode.com/problems/subarray-product-less-than-k/
"""
import bisect
import math
bisect.bisect()

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        log_nums = [math.log(num) for num in nums]
        log_k = -1 if k < 1 \
            else math.log(k-.5)

        cum_log_nums = [0]
        for log_num in log_nums:
            cum_log_nums.append(cum_log_nums[-1] + log_num)

        n_products = 0
        i = 0
        j = 1
        while i < len(cum_log_nums):
            if j <= i:
                j = i + 1

            if j == len(cum_log_nums) or cum_log_nums[j] - cum_log_nums[i] > log_k:
                n_products += j - 1 - i
                i += 1
            else:
                j += 1

        return n_products

    def numSubarrayProductLessThanK_old(self, nums: list[int], k: int) -> int:
        log_nums = [math.log(num) for num in nums]
        log_k = log_k = -1 if k < 1 \
            else math.log(k-.5)

        cum_log_nums = [0]
        for log_num in log_nums:
            cum_log_nums.append(cum_log_nums[-1] + log_num)

        n_products = 0
        for i in range(len(cum_log_nums)):
            for j in range(i + 1, len(cum_log_nums)):
                if cum_log_nums[j] - cum_log_nums[i] < log_k:
                    n_products += 1
                else:
                    break
        return n_products



if __name__ == "__main__":
    res = Solution().numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100)
    assert res == 8

    res = Solution().numSubarrayProductLessThanK(nums = [1, 2, 3], k = 0)
    assert res == 0

    res = Solution().numSubarrayProductLessThanK(
        nums = [10,3,3,7,2,9,7,4,7,2,8,6,5,1,5], k = 30)
    assert res == 26

    print(f"all done")
