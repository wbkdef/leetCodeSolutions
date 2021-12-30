from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        print(f"{graph=}")
        return self._allPathsSourceTarget(graph, 0)

    def _allPathsSourceTarget(self, graph: List[List[int]], ind: int) -> List[List[int]]:
        if ind == len(graph) - 1:
            print(f"if {ind=}")
            return [[ind]]
        res = [[ind] + path
               for n in graph[ind]
               for path in self._allPathsSourceTarget(graph, n)
               ]
        print(f"{ind=}, {res=}")
        return res


s = Solution()
Input = [[1, 2], [3], [3], []]
Output = [[0, 1, 3], [0, 2, 3]]
res = s.allPathsSourceTarget(Input)
assert Output == res

# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

s = Solution()
Input = [[4,3,1],[3,2,4],[3],[4],[]]
Output = [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
res = s.allPathsSourceTarget(Input)
assert Output == res

print(f"All Done")