class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        for i in range(len(nums)+1):
            if i not in nums:
                ans=i
        return ans        
