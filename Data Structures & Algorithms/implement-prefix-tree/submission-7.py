class Node:
    def __init__(self):
        self.sons = dict()
        self.is_end = False

class PrefixTree:
    # The idea is to build a tree in which each node
    # can have multiple sons, when we walk the tree we walk through 
    # prefixes we start from the first node which has not associate letters
    # each node have a dict with mapping letters->son and each node have a set of strings
    # that are made of that prefix walk

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        # I have to walk through the prefix tree
        # if there are no nodes i have to add them, until i reach the end, and then
        # at the end i add the string to the last node
        #print("Doing Insert")
        currNode = self.root
        for ch in word:
            nextNode = currNode.sons.get(ch, None)
            if not nextNode:
                temp = Node()
                currNode.sons[ch] = temp
                nextNode = temp
                currNode = temp
            else:
                currNode = nextNode
        currNode.is_end = True
                



    def search(self, word: str) -> bool:
        #print("Doing Search")
        currNode = self.root
        for ch in word:
            nextNode = currNode.sons.get(ch, None)
            if not nextNode:
                return False
            else:
                currNode = nextNode
        return currNode.is_end

        

    def startsWith(self, prefix: str) -> bool:
        #print("Doing stat with")
        currNode = self.root
        for ch in prefix:
            nextNode = currNode.sons.get(ch, None)
            if not nextNode:
                return False
            else:
                currNode = nextNode
        return True

        
        