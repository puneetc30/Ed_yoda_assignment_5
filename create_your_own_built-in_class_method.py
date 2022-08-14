class Solution:
    def power(self,x,n):
        return x**n

x = int(input("Enter a number: "))
n = int(input("Enter the power: "))
print(Solution().power(x,n))