class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 1 if n != 0 else 0
        a, b, c = 0 , 1 , 1
        s = a+b+c
        for i in range(3, n+1):
            s = a + b + c
            a= b
            b= c
            c = s
        return s