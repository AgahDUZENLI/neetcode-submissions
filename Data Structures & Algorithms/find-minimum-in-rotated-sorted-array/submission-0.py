class Solution:
    def findMin(self, nums: List[int]) -> int:
        lenght = len(nums)
        left, right = 0, lenght-1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            
        return nums[left]

        