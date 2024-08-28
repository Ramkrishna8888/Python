n = int(input("Enter a number: "))
count = 0

if n <= 1:
    count = 1
else:
    for i in range(2, n):
        if n % i == 0:
            count += 1

if count == 0:
    print("This is a prime number.")
else:
    print("This is not a prime number.")
