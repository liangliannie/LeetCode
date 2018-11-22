class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)<=0:
            return -1
        if len(nums)==1 and target == nums[0]:
            return 0
        else:
            return -1
        
        n = len(nums)
        start = nums[:n/2]
        end = nums[n/2:]
        print(start,end)
        left = self.search(start,target)
        if left >=0:
            return left
        right = self.search(end,target)
        if right>=0:
            return right + n/2
        
        return -1
    
s=Solution()
nums = [4,5,6,7,0,1,2]
target = 0
s.search(nums, target)