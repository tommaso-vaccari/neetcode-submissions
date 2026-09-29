class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # I have an array that was sorted in ascending order 1,2,3,4,5,6
        # trivial solution to scan the array in search for the target
        # I need to understand what does it mean that it has been rotated
        # If i can restore the rotation then i can perform a binary search on
        # the array that runs in log(n)
        # I can immagine rotation as if they were pushing the element on the righ and we have 
        # overlap on the array.
        # I search for the old start and end point of the array i have already a linear
        #scan that is not worth it.
        # Ok now i see the thing, classic bynary search, i choose a starting point
        # which is in the middle of the array, i can then check if the target is in the 
        # range of the two subarray.
        # immagine starting with m as middle point:
        # l = 0, m = 2, r = 5
        # if(arr[l] < arr[m]) -> classic scenario for understanding if t is there
        # else(arr[l] > arr[m]) ---> t is there is it's bigger than the left, but if 
        # More simpler, i just need to ask if the target it's in some way between the two
        # numbers assuming uniqueness
        
        if not nums:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        arr = nums
        while left <= right:
            
            m = (left + right ) // 2
            if target== nums[m]:
                return m

            if nums[left] <= nums[m]:  # left half is sorted
                if nums[left] <= target < nums[m]:
                    right = m - 1
                else:
                    left = m + 1
            else:                       # right half is sorted
                if nums[m] < target <= nums[right]:
                    left = m + 1
                else:
                    right = m - 1

        return -1

            


            





        