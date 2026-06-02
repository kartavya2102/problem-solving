# Floyd’s Triangle is a pattern of consecutive natural numbers arranged in rows, where the i-th row contains i numbers.

# Examples:

# Input: n = 4
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10


n = int(input("Enter your num : "))
num = 1
# code here
for i in range(1,n+1):
    for j in range (i):
        print(num , end = " ")
        num +=1
        
    print()