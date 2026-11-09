class Node:
    def __init__(self, key=None, value=None, prev=None, succ = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.succ = succ

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = dict() #Storing key->node pointer
        self.dh = Node()
        self.dt = Node()
        self.dt.succ = self.dh
        self.dh.prev = self.dt
        self.capacity = capacity
        self.dim = 0
        # dt <->    <->dh
        

    def get(self, key: int) -> int:
        #print("get", key)
        #print(self.dic)
        #First if the key is not there return -1
        if key not in self.dic:
            return -1
        #Retrieve the node
        node = self.dic[key]
        #Retrieve the value
        val = node.value
        #Now i have to put as first node this one that i have just accessed

        previousNode = node.prev
        nextNode = node.succ

        #Link togethere the two
        previousNode.succ = nextNode
        nextNode.prev = previousNode

        #Now i have to update the head
        # So i gather the current head with the prev on the dummy head
        # and i put that the successive on the current head is the node that
        # i have removed
        exHead =  self.dh.prev
        exHead.succ = node
        node.prev = exHead
        node.succ = self.dh
        self.dh.prev = node
        
        return val
        
         
    def put(self, key: int, value: int) -> None:
        #If the key is already there i do not have to incremenet the dim
        # and just move as head of the group the node, otherways i can create and put it as head of the
        # group
        #print("Put",key,value)
        
        if key not in self.dic:
            # i have to add it and check for capacity, i may have to drop
            # the last node
            self.dim+=1
            if self.dim > self.capacity:
                # Drop last node and decrement dim
                toDrop = self.dt.succ
                #print("Exceed capacity")
                #print(toDrop.value,toDrop.key)
                
                del self.dic[toDrop.key]
                
                toDrop.succ.prev = self.dt
                self.dt.succ = toDrop.succ
                self.dim-=1
            # Now i have to insert the new node as head
            node = Node(key = key, value = value)
            self.dic[key] = node
            exHead =  self.dh.prev
            exHead.succ = node
            node.prev = exHead
            node.succ = self.dh
            self.dh.prev = node
        else:
            # I just need to update the node value and move it to the head
            node = self.dic[key]
            node.value = value
            previousNode = node.prev
            nextNode = node.succ

            #Link togethere the two
            previousNode.succ = nextNode
            nextNode.prev = previousNode

            #Now i have to update the head
            # So i gather the current head with the prev on the dummy head
            # and i put that the successive on the current head is the node that
            # i have removed
            exHead =  self.dh.prev
            exHead.succ = node
            node.prev = exHead
            node.succ = self.dh
            self.dh.prev = node
        #print(self.dic)






        

        