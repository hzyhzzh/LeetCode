class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x == z or y == z or x + y == z: return True
        if z > x + y: return False

        # y should always be the larger jars
        if x > y: x, y = y, x

        # fill both with the capacity of the smaller jar
        jug_x, jug_y = x, x

        while not (jug_x == 0 and jug_y == 0):
            # jug_x -> jug_y
            tmp = jug_x
            jug_x = abs(min((y - jug_y) - jug_x, 0))
            jug_y = min(jug_y + tmp, y, y)

            # check
            if jug_x == z or jug_y == z or jug_x + jug_y == z:
                return True

            # empty jug_y if it is full
            if jug_y == y:
                jug_y = 0
                continue

            # fill jug_x
            jug_x = x

        return False
