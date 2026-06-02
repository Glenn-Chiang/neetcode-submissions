class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[end]:
                if target > nums[end] or target < nums[mid]:
                    # search left
                    end = mid - 1
                else:
                    # search right
                    start = mid + 1
            elif nums[mid] >= nums[end]:
                if target < nums[start] or target > nums[mid]:
                    # search right
                    start = mid + 1
                else:
                    # search left
                    end = mid - 1
        return -1
