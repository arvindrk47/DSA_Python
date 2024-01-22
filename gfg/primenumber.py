#User function Template for python3

class Solution:
    def isPrime (self, N):
        # code here
        ct = 0

        # Iterate through numbers from 1 to the square root of N
        for i in range(1, int(N**0.5) + 1):
            # Check if i is a divisor of N
            if N % i == 0:
                ct += 1
                # If i is not the square root of N, add N/i as another divisor
                if N // i != i:
                    ct += 1

        # If the number of divisors is 2, return 1 (indicating prime), else return 0
        if ct == 2:
            return 1
        else:
            return 0
            
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends