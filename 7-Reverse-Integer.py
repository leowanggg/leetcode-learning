class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            xs = str(x)
            xs = xs[::-1]
            _x = int(xs)
        elif x < 0:
            xs = str(-1*x)
            xs = xs[::-1]
            _x = -1 * int(xs)
        elif x == 0:
            _x = 0
        if _x > 2147483647 or _x < -2147483647:
            _x = 0
        return _x
