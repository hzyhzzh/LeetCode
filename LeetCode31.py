class Solution(object):
    def search(self, nums, start, end, target):
        # binary search to get the index which is the smallest one larger than
        # target
        low, high = start, end
        while low <= high:
            mid = low + high >> 1
            if nums[mid] <= target:
                high = mid - 1
            else:
                if mid == end or nums[mid + 1] <= target:
                    return mid
                low = mid + 1

    def reverse(self, nums, start, end):
        # reverse the nums[start:end + 1] in place
        low, high = start, end
        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1

    def nextPermutation(self, nums):
        n = len(nums)
        if n <= 1:
            return

        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1

        if i >= 0:
            x = self.search(nums, i + 1, n - 1, nums[i])
            nums[i], nums[x] = nums[x], nums[i]

        self.reverse(nums, i + 1, n - 1)
