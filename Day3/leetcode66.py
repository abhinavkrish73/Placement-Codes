class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in digits :
            num = num * 10 + i
        num+=1
        digits=[]
        while(num!=0):
            dig = num % 10
            digits.append(dig)
            num = num // 10
        digits.reverse()
        return digits

