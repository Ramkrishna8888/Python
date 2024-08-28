print("Enter an integer")
n=int(input())
s=0
while(n>0):
        dig=n%10
        s=s+dig
        n=n//10
print(s)
