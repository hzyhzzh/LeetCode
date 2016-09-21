class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        width, num, digit, k = 1, 9, 0, 0

        while n > digit + width * num:
            digit += width * num
            k += num
            width += 1
            num *= 10

        n -= digit
        k += (n-1) // width + 1
        pos = (n-1) % width
        return int(str(k)[pos])
