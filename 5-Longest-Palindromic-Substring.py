class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        for i in range(N+1)[::-1]:
            for j in xrange(N-i+1):
                substring = s[j:j+i]
                if substring == substring[::-1]:
                    return substring
