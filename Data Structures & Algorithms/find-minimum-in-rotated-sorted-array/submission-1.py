class Solution:
    def findMin(self, nums: List[int]) -> int:
        #UMPIRE : Understand Match Plan Implement Review and Evaluate
        # I need to find the minimum in the array that was sorted but rotated.
        # This brings me an idea, i know that in this array there is only one point in which 
        # the ordering is break and it's the point in which we find consequentialy the
        # max and the min of the array. The first idea on top of my mind
        # it so keep searching in the non ordered part of the array.
        # In the non orderered part of the array I am sure that i will find the minimum
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            if left == right:
                return nums[left]

            m = (left + right) // 2

            # I want to keep searching in the non ordered half of the array

            if nums[left] > nums[m]:
                # the left part is the one that it's not ordered 
                right = m 
            elif nums[m] > nums[right]:
                left = m + 1
                # the right part it's not ordered
            else:
                # the array is ordered, where do i need to search? 
                # classical bynary search
                # but with a sorted array, the min is at the left
                right = m




        # I notice that i had used >= this was not working, why it's right as it is?