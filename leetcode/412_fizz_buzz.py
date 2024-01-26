class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        temp = list()
        for i in range(1,n+1):
            if i%3 ==0 and i%5 == 0:
                temp.append("FizzBuzz")
            elif i%5 == 0:
                temp.append("Buzz")
            elif i%3 == 0:
                temp.append("Fizz")
            else:
                temp.append(f"{str(i)}")
        return temp
    

        