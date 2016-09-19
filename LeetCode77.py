import itertools
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        element = []
        for i in range(1, n+1):
            element.append(i)
        result = []
        for i in itertools.combinations(element,k):
            result.append(i)

        return result
