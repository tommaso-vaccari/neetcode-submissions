class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        #Maximum number of client that can be satifies i have at maximum
        # a certain number of jolly that i can use, called minutes
        if not grumpy or not customers:
            return 0

        if sum(grumpy) == 0:
            return sum(customers)
        if not grumpy or not customers:
            return 0

        # I need to choose a sliding window of being not grumpy that maximizes the clients
        actual_served = list()
        not_grumpy = list()
        for i in range(len(customers)):
            not_grumpy.append(1 if grumpy[i] == 0 else 0 )
            actual_served.append(customers[i] * not_grumpy[i])
        

        starting = 0
        final = 0 #included or not?
        max_clients = 0
        for i in range(len(customers)-minutes+1):
            normal_clients_served = sum(actual_served[i:i+minutes])
            without_being_grumpy = sum(customers[i:i+minutes])
            #print(i, i+minutes, actual_served, actual_served[i:i+minutes], without_being_grumpy,normal_clients_served)
            if without_being_grumpy - normal_clients_served > max_clients:
                max_clients = without_being_grumpy
                starting = i
                final = i + minutes




        #print(starting, final)
        total_served = 0
        i = 0
        while i < starting:
            #print(i)
            total_served += customers[i] * not_grumpy[i]
            i+=1
        #print(total_served)
        total_served += sum(customers[starting:final])
        #print(total_served)
        for j in range(final, len(customers)):
            #print(j)
            total_served += customers[j] * not_grumpy[j]
        #print(total_served)
        return total_served

            

#customers = [1,0,1,2,1,1,7,5]
#   grumpy = [0,1,0,1,0,1,0,1]

# total = 0 + 0 + 0 + 2 + 0 + 1 + 7 + 5 = 



            




        