'''write a program to find the reverse of the given number
'''

def reverse(num):
    
  rev=0
  while(num>0):
    rev= rev*10+num%10
    num//=10
  return rev

def ispalindrome(num):
    rev=reverse(num)
    return num==reverse(num)

print(reverse(123))
print(ispalindrome(1239))
print(reverse(121))
print(ispalindrome(121))

def getPalindromes(start,end):
  res=""
  for i in range(1,end+1):
    if ispalindrome(i):
      res=res+str(i)+","
  return res
print(getPalindromes(1,1000))
