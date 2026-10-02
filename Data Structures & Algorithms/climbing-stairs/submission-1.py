class Solution:
    def climbStairs(self, n: int) -> int:
        #The subproblem: what does ways(i) mean? Write it in one precise sentence, for example 
        #"the number of distinct ways to reach step $i$".
        #The recurrence: to reach step $i$, what could your last move have been? 
        #From that, how does ways(i) depend on smaller values?
        #The base cases: for which values of $i$ do you know ways(i) without computing anything?

        # UMPIRE
        # I see some sort of recursion, at each step i can choose two approaches
        # if i have enough room i can do a 2 step, or 1 step, 

        options = [-1] * n
        def numOfOptions(step):
            if step+1 == n:
                return 1
            if step+2 == n:
                return 2
            if options[step+1]==-1: options[step+1] = numOfOptions(step+1) 
            if options[step+2]==-1: options[step+2] = numOfOptions(step+2)

            return options[step+1] + options[step+2]
        return numOfOptions(0)

        
        