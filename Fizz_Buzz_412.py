class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rtype = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                rtype.append("FizzBuzz")
            elif i % 3 == 0:
                rtype.append("Fizz")
            elif i % 5 == 0:
                rtype.append("Buzz")
            else:
                rtype.append(str(i))

        return rtype


Solution.fizzBuzz(None, 3)
Solution.fizzBuzz(None, 5)
Solution.fizzBuzz(None, 15)  # 15 only returns fizz and not fizzbuzz as it should
