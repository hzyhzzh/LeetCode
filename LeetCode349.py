class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result =[]
        for n1 in nums1:
            if(n1 in nums2 and n1 not in result):
                result.append(n1)

        return result
