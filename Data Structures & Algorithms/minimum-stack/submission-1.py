class MinStack:
    # I need to do all in costant time
    # and i need to pop the minimum
    # the problem is that when I pop an element
    # which may be the minimum i need to update the current min
    # a min heap has costs that are way more than cpstants so i
    # cannot use it.
    # I can use a combination of ds to obtain something that keeps the minimum in some
    # way reachable, i need to know in some way the element that i have and the current min

    def __init__(self):
        self.stack = list()
        self.min = float("+inf")

    def push(self, val: int) -> None:
        
        self.min = min(self.min, val)
        self.stack.append([val, self.min])
        
        
        

    def pop(self) -> None:
        #if the element that i pop is the min, which should be the new min value?
        # i should in some way maintain knowledge of the magnitude of the elements
        # i should have for each element the correspondent min saved iin some way.
        print("pop")
        
        self.stack.pop()
        if len(self.stack)==0:
            self.min = float("+inf")
        else:
            self.min = self.stack[-1][1]
        

    def top(self) -> int:
        print("top")
        return self.stack[-1][0]

    def getMin(self) -> int:
        print("getmin")
        return self.stack[-1][1]

#Debug by hand Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"
# 1) []
# 2) [[1,1]]
# 3) [[1,1],[2,1]]
# 4) [[1,1],[2,1],[0,0]]
        
