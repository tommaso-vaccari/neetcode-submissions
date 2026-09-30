class RandomizedSet:

    def __init__(self):
        #I cannot use a set given that for random i need to use a list
        # I can use instead a dict for mapping the element to their
        # index
        self.array = list()
        self.mapping = dict()
        

    def insert(self, val: int) -> bool:
        if val not in self.mapping:
            self.array.append(val)
            self.mapping[val] = len(self.array) - 1
        

    def remove(self, val: int) -> bool:
        if val in self.mapping:
            temp = self.array[-1]
            self.array[self.mapping[val]] = temp
            self.mapping[temp] = self.mapping[val]
            self.array.pop()
        

    def getRandom(self) -> int:
        index = random.randint(0, len(self.array)-1)
        return self.array[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()