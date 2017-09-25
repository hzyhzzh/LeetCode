# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        size = len(points)
        if size  < 3:
            return size
        ans = 0
        for i in range(size):
            d = {'inf':0}
            samePoint = 1
            for j in range(size):
                if i == j:
                    continue
                elif points[i].x == points[j].x and points[i].y != points[j].y:
                    d['inf'] += 1
                elif points[i].x != points[j].x:
                    k = 1.0 * (points[i].y - points[j].y) / (points[i].x - points[j].x)
                    if k in d:
                        d[k] += 1
                    else:
                        d[k] = 1
                else:
                    samePoint += 1
            ans = max(ans,max(d.values()) + samePoint)
        return ans