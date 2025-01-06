class Solution(object):
    def isPalindrome(self, x):
        reversed = 0
        num = x

        while (num > 0):
            remainder = num % 10
            reversed = reversed * 10 + remainder

            num = num // 10
            
        return x == reversed

        