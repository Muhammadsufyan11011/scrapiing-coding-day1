print("hello wrold"
a = 22
b = 32
c = 44
code = 3
sum=a+b+c/code
print(sum)


def hary(month1,month2,month3):
	total=month1+month2+month3
	return total/3
average=hary(22,44,66)
print(hary(3,6,3))


code=[33,54,35]
ave=sum(code)/len(code)
print(ave)

number=[5,3,2,1]
number.sort()
print(number)





class Solution:
    def isAnagram(self, s: str, t: str):
        counter(S)==counter(T)
        if len(s)!= len(t):
            return false
        countS,countT={},{}
        for i in range(len(s)):
            countS[s[i]]=1 + countS.get(s[i],0)
            countT[t[i]]=1 + countT.get(t[i],0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True


a1len(a1)==len(a2):
=input("Enter a first word:")
a2=input("Enter a secend word:")
if a1_sorted=sorted(a1)
	a2_sorted=sorted(a2)
	if a1_sorted == a2_sorted:
		print("it is anagram")
	else:
		print("it is not anagram")
else:
	print("it is not anagram")


def anagram(a1,a2):

	

	if len(a1)==len(a2):

		return True
	else:
		return False
a1="code"
a2="Eeco"
print(anagram(a1,a2))

def isPowerOfFour(n):
    if n <= 0:
        return False
    while n % 4 == 0:
        n //= 4
    return n == 1

# Example
n = 16
print(isPowerOfFour(n))  

"""powe of four  divisin"""



def PowerFour(n):
    if n == 1:
        return True
    if n <= 0 or n % 4 != 0:
        return False
    return 	PowerFour(n // 4)
n = 64

print(PowerFour(n)) 


