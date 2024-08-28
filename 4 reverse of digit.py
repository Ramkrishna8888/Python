print("Enter an integer")
n=int(input())
reverse=0
while(n>0):
        dig = n%10
        reverse=reverse*10+dig
        n=n//10
print(reverse)
