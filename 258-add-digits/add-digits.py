class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>=10:
            digit=num%10
            num=num//10 
            num=num+digit
        return num           