"""
From: https://leetcode.com/problems/course-schedule-ii/
"""

import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # return self.brute_force(numCourses,  prerequisites)
        return self.blockerless(numCourses,  prerequisites)

    def brute_force(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        courses_schedule_order = []
        courses_scheduled = set()
        courses_not_scheduled = set(range(numCourses))

        # if not courses_not_scheduled:
        #     return courses_schedule_order
        while courses_not_scheduled:
            courses_to_schedule = set(courses_not_scheduled)
            for post, pre in prerequisites:
                if post in courses_to_schedule and pre in courses_not_scheduled:
                    courses_to_schedule.remove(post)
            if not courses_to_schedule:
                # Can't schedule any
                return []
            courses_schedule_order += sorted(courses_to_schedule)
            courses_not_scheduled -= courses_to_schedule
        return courses_schedule_order

    def blockerless(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        Q = set(range(numCourses))
        G = collections.defaultdict(set)
        n_blockers = collections.defaultdict(int)
        for post, pre in prerequisites:
            Q -= {post}
            G[pre].add(post)
            n_blockers[post]+=1

        topological_ordering = []
        while Q:
            ind = next(iter(Q))
            topological_ordering.append(ind)
            Q.remove(ind)
            for ind2 in G[ind]:
                n_blockers[ind2] -= 1
                if n_blockers[ind2] == 0:
                    Q.add(ind2)

        if len(topological_ordering) < numCourses:
            return []
        return topological_ordering



if __name__ == "__main__":
    res = Solution().findOrder(numCourses = 2, prerequisites = [[1,0]])
    assert res == [0,1]

    res = Solution().findOrder(numCourses = 4,
                               prerequisites = [[1,0],[2,0],[3,1],[3,2]])
    assert res == [0,1,2,3]

    res = Solution().findOrder(numCourses = 1, prerequisites = [])
    assert res == [0]

    res = Solution().findOrder(numCourses = 4,
                               prerequisites = [[1,0],[2,0],[3,1],[1,2], [2, 3]])
    assert res == []

    print(f"All done")