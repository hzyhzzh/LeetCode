class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        tmp = []
        for i in range(len(nums1)):
            try:
                index = nums2.index(nums1[i])
            except ValueError:
                continue
            else:
                if(nums2[index] not in tmp):
                    count2 = nums2.count(nums2[index])
                    count1 = nums1.count(nums2[index])
                    count = min(count1, count2)
                    for i in range(count):
                        tmp.append(nums2[index])

        return tmp
