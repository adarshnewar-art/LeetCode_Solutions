class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
 
        """
        c=0
        copy=word
        while word in sequence:
            c+=1
            word+=copy
        return c