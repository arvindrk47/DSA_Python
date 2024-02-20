class Solution:

    def counts(self, num):
        ld, temp=0,0,
        while(num>0):
            ld = num%10
            temp+=ld
            num=num//10
        return temp
    def addDigits(self, num: int) -> int:
        while(num>9):
            num = self.counts(num)
        return num
        