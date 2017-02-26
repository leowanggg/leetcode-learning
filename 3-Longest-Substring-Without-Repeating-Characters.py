class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = ""
        longest_substring_length = 0
        for i in s:
            if i in substring:
                if len(substring) > longest_substring_length:
                    longest_substring_length = len(substring)
                substring = substring[substring.find(i)+1:] + i
            else:
                substring += i
        if longest_substring_length == 0:
            longest_substring_length = len(s)
        elif len(substring) > longest_substring_length:
            longest_substring_length = len(substring)
        return longest_substring_length
