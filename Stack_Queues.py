class StackWithQueues:
    def __init__(self):
        self.q1 = [] #listing of the both stacks 
        self.q2 = []

    def push(self,x):
        self.q2.append(x) #push to the q2 

    #move to q2 from q1 

        while self.q1:
            self.q2.append(self.q1.pop(0))   #pop(0) mimics queue behavior 

        self.q1 , self.q2  = self.q2, self.q1

    def pop(self):
        if not self.q1:
            return -1  #edge case: if the stack is empty
        return self.q1.pop(0) 
    
    def top(self):
        if not self.q1:
            return -1
        return self.q1[0]
    

    def is_empty(self):
        return len(self.q1) ==0 



stack = StackWithQueues()
stack.push(3)
stack.push(2)
stack.push(5)
print(stack.top())     
print(stack.pop())       
print(stack.is_empty())