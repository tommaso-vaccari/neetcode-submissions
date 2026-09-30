from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #UMPIRE
        # U I need to build the maximum number of substring while ensuring
        # that each letter appears at most in one substring. 
        # M at first glance it does not match any pattern that I already know
        # 

        if not str :
            return 0

        res = list()

        left,right = 0,0

        positions = defaultdict(list)

        # Need to build ds needed
        # I need a dict that maps char-> index in which it appears in the seuqnece
        # and then i need a seen set rolling on the current interval
        j = 0
        for i in range(len(s)):
            positions[s[i]].append(i)
        
        while left < len(s):
            # I start with the character in position s[left]
            # Now i have to extend the right at least untile the last appearence of that 
            # character
            expanded = set()
            not_yet_expanded = set()
            expanded.add(s[left])
    
            right = max(positions[s[left]])
            

            # Now my tempative substring is this one, 
            # notice that now i have to expand with the maximum length provided by
            # the character that appears in the farest position
            # but this can lead to me to introducing new characters
            # So i have to iteratively expand until I have expanded all of them
            # I have to build the set of not_yet_expanded that is given by
            # the char that are in the string but not in expanded
            
            while True:
                
                for c in s[left:right+1]:
                    if c not in expanded:
                        not_yet_expanded.add(c)
                #print(s[left:right+1])
                #print(not_yet_expanded)
                if not not_yet_expanded: 
                    # I am questioning this one, give that maybe 
                    #after the expansion we may have new char
                    break

                to_expand = not_yet_expanded.pop()
                right = max(right, max(positions[to_expand]))
                expanded.add(to_expand)

            

            
            res.append(right+1-left)
            # Now i have to update for the new search
            left = right + 1
           

        return res








        