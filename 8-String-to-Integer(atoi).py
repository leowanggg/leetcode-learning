class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        s = ""
        sign = 1
        if str.isspace() or str == "":
            return 0
        if len(str) == 1 and not str.isdigit():
            return 0
        while i < len(str) and str[i].isspace():
            i += 1
        if i < len(str) and str[i] == "+":
            sign = 1
            i += 1
        elif i < len(str) and str[i] == "-":
            sign = -1
            i +=1
        if not str[i].isdigit():
            return 0
        while i < len(str) and str[i].isdigit():
            s += str[i]
            i += 1
        s_int = sign * int(s)
        if s_int > 2147483647:
            s_int = 2147483647
        elif s_int < -2147483648:
            s_int = -2147483648
        return s_int
