class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [
        num for num in range(left, right + 1)
        if all(d != '0' and num % int(d) == 0 for d in str(num))
        ]
        