class Node:
    def __init__(self, letter = "---"):
        self.letter = letter
        self.sons = dict()
        self.words = set()

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
        def walk_insert(st, node):
            
            if len(st)==0:
                # i have reached the node in which i have to insert
                node.words.add(word)
                return 
            
            next_node = node.sons.get(st[0], None)
            if next_node is None:
                temp = Node(st[0])
                node.sons[st[0]] = temp
                next_node = temp
                
            return walk_insert(st[1:],next_node)
        
        return walk_insert(word,self.root)
                



    def search(self, word: str) -> bool:
        #print("Doing Search")
        def walk_search(st, node):
            if len(st)==0:
                #print(word in node.words)
                return word in node.words
            
            next_node = node.sons.get(st[0], None)

            if next_node is None:
                return False
            
            return walk_search(st[1:],next_node)
        
        return walk_search(word,self.root)

        

    def startsWith(self, prefix: str) -> bool:
        #print("Doing stat with")
        def walk_search(st, node):
            if len(st)==0:
                return len(node.sons) > 0 or prefix in node.words
            
            next_node = node.sons.get(st[0], None)

            if next_node is None:
                return False
            
            return walk_search(st[1:],next_node)
        
        return walk_search(prefix,self.root)

        
        