class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindroms = []
        palindroms.append({(i, i) for i in range(len(s)+1)})
        palindroms.append({(i, i+1) for i in range(len(s))})
        # print(palindroms[0])
        # print(palindroms[1])

        while palindroms[-1] or palindroms[-2]:
            palindroms.append(set())
            for i, j in palindroms[-3]:
                if i-1 >=0 and j+1 <= len(s) \
                        and s[i-1] ==  s[j]:
                    palindroms[-1].add((i-1, j+1))
            # print(palindroms[-1])
        i, j = next(iter(palindroms[-3]))
        return s[i: j]

if __name__ == "__main__":
    s = "babad"
    res = Solution().longestPalindrome(s)
    assert res in ["bab", "aba"]

    s = ""
    res = Solution().longestPalindrome(s)
    assert res in [""]

    s = "cbbd"
    res = Solution().longestPalindrome(s)
    assert res in ["bb"]

    s = "a"
    res = Solution().longestPalindrome(s)
    assert res in ["a"]

    s = "ac"
    res = Solution().longestPalindrome(s)
    assert res in ["a", "c"]

    s = "babbad"
    res = Solution().longestPalindrome(s)
    assert res in ["abba"]

    s = "bababadad"
    res = Solution().longestPalindrome(s)
    assert res in ["ababa"]

    print(f"All done")