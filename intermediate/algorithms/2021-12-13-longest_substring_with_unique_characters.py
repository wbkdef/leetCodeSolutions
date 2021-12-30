class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrs = {(i, i+1) for i in range(len(s))}

        while substrs:
            print(f"{substrs=}")
            substrs_next = set()
            for i, j in substrs:
                if (i+1, j+1) in substrs:
                    if s[i] != s[j]:
                        substrs_next.add((i, j+1))
            if not substrs_next:
                break
            substrs = substrs_next
        i, j = next(iter(substrs))
        return j-i

if __name__ == "__main__":
    s = "abcabcbb"
    sol = Solution()
    assert sol.lengthOfLongestSubstring(s) == 3
