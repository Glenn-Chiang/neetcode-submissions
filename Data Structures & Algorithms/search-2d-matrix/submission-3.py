class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1

        def search_1d(arr):
            low = 0
            high = len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    high = mid - 1
                elif arr[mid] < target:
                    low = mid + 1
            return False

        while low <= high:
            mid = (low + high) // 2
            arr = matrix[mid]
            
            # If target is in array range
            if arr[0] <= target and target <= arr[-1]:
                return search_1d(arr)

            # If target is less than first element of array, search left
            elif target < arr[0]:
                high = mid - 1

            # If target is greater than last element of array, search right
            elif target > arr[-1]:
                low = mid + 1

        return False