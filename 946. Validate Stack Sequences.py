from setuptools.sandbox import pushd
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        push_pointer = 0
        popped_pointer = 0
        while popped_pointer<len(popped):
            while push_pointer < len(pushed) and pushed[push_pointer]!=popped[popped_pointer]:
                push_pointer +=1
            if push_pointer >= len(pushed):
                return False    
            pushed[push_pointer] = -1
            while push_pointer>=0 and pushed[push_pointer] ==-1:
                push_pointer-=1
            popped_pointer+=1 
        return True
    
    def validateStackSequences2(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        j = 0 
        stack=[]
        for n in pushed:
            stack.append(n)
            while stack and stack[-1]==popped[j]:
                stack.pop()
                j+=1
#         print(stack)
        return not stack
       
        
s=Solution()
pushed = [1,2,3,4,5]
popped = [4,3,5,2,1]
print(s.validateStackSequences2(pushed, popped))
pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
print(s.validateStackSequences2(pushed, popped))
