#num = [7, 8, 120, 25, 44, 20, 27]
#num1 = [x for x in num if x % 2 != 0]
#print(num)
#print(num1)
n=[23,7,6,6]
c=0
for i in n:
    f =0
    for j in range(2,i):
        if(i%j == 0):
            f=1
            break;
        if(f==0):
            c=c+1
if (len(n)==c):
    print("Correct")
else:
    s=0
    for i in n:
        s=s+i
    f=1
    for j in range(2,s):
        if(s%j==0):
            print("In-Correct")
            f=0
            break
        if(f==1):
            print("Correct")
