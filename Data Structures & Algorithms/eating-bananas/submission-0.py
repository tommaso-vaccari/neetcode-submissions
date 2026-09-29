from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #UMPIRE
        # I need to find the minimum k for which i can eat all the 
        # bananas in h hours. Problem: I cannot assume continuos
        # consumption, that means that if i have finished the pile in less
        # the one hour i still have to dedicate the entire hour to that
        # pile

        # Upper bound for the answer is k = h, i must have least
        # the time to eat all the bananas using k = 1

        # Since the upper bound is

        upper_bound = max(piles)

        # Now i can try a bynary search to get the value
        left = 1
        right = upper_bound

        # I need a fast way to compute how many hours i need 
        # given the k rate chosen
        it = 0
        while left <= right:
            m = (left+right) // 2
            if left == right:
                return left
            print(right, left)
            # m is the temptative k, i need to calculate how many
            # hours it takes with the chosen m

            hours = 0

            for i in piles:
                hours += ceil(i/m)

            #This mean that i am faster than what 
            # is required so i can try to choose a 
            #lower m       

            if hours <=h: 
                right = m
            else:
                # I am slower i need to go faster
                left = m + 1
       

                



