from math import ceil
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #UMPIRE : Understand Match Plan Implement Review Evaluate
        # I need to return a number, the least weight capacity
        # of the ship that permits to ship all the packages in d days.

        # The idea is to work as in the koko problem using binary search 
        # on an interval. I need to find a feasable upper bound
        # for the weight capacity that gaves me the possibility to ship in that days,
        # and maybe also a lower bound

        # Given that i have at least one day to ship, the upper bound is the sum 
        # of all the packages.
        total_weights = sum(weights)
        right = total_weights
        
        # With this capacity i can ship everything in a single day

        # Now i need a lower bound for the problem, 
        # given that it cannot be neither 0 or zero, otherwise i will need at least
        # oh oh stop for a moment, yes i have an upper bound and that all that matters, 
        # i can just use 1 as lower bound given that if it's not enough than i am going to
        # move the search in another area


        left = max(weights)


        # given the capacity of the ship, how many days will it take to ship them? 

        
        j = 0
        while left <= right:
            j+=1
            if left == right:
                return left

            capacity = (left + right) // 2
            print(left, capacity, right)
            days_needed = 0 

            i = 0
            acc = weights[0]
            while i < len(weights)-1:
                if acc + weights[i+1] <= capacity :
                    acc += weights[i+1]
                    
                else:
                    # I need to ship another day the package
                    acc = weights[i+1]
                    days_needed +=1
                i+=1
            if acc!= 0 : days_needed+= ceil(acc/capacity)  
            
            
            print(days_needed)
            
            if days_needed <= days: # I have room to decrease the capacity
                right = capacity
            else:
                # Too slow i need to increase the capacity
                left = capacity + 1
     








        