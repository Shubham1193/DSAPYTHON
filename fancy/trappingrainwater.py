class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else : 
            return "stack is empty"
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        return self.stack
    
def leftmax(height):
    ans = []
    max = 0
    for i in height:
        ans.append(max)
        if i > max :
            max = i
    return ans

def rightmax(height):
    ans = []
    max = 0
    for i in range(len(height) - 1 , -1  , -1):
        ans.append(max)
        if height[i] > max :
            max = height[i]
    return list(reversed(ans))


# left max max = -inift from oth pos set leftmax is -inif and chcek if curr is greter than max if yes then set max to that for the building that is about to come
# 
#  

if __name__ == "__main__":
    height = [3, 0, 2, 0, 4]
    leftwall = leftmax(height)
    print(leftwall)
    rightwall = rightmax(height)
    print(rightwall)
    water = 0
    for i in range(0  , len(height)):
        min = 0
        if leftwall[i] < rightwall[i]:
            min = leftwall[i]
        else : 
            min = rightwall[i]
        # water = height[i] - min
        if min == 0:
            water += 0
        else :
            water += min - height[i]

    print(water)
# water on bar is min on leftwall rightwall  - height and if min is o then water is 0 
    # print(water