"""
From: https://leetcode.com/problems/generate-parentheses/
PC:KEYfNFs:
"""
import functools


class Solution:

    @functools.cache
    def generateParenthesis(self, n: int) -> list[str]:
        assert n >= 0
        assert isinstance(n,  int)

        if n == 0:
            return [""]

        pars = set()
        for pars_nm1 in self.generateParenthesis(n-1):
            pars.add(f"({pars_nm1})")
        for i in range(1, n):
            for pars_i in self.generateParenthesis(i):
                for pars_nmi in self.generateParenthesis(n-i):
                    pars.add(f"{pars_i}{pars_nmi}")

        return sorted(pars)



if __name__ == "__main__":
    res = Solution().generateParenthesis(1)
    assert res == ["()"]

    res = Solution().generateParenthesis(3)
    assert res == ["((()))","(()())","(())()","()(())","()()()"]

    print(f"All done")