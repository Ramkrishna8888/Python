print("Enter an integer")
n = int(input())
original_n = n  # Store the original number
reverse = 0

while n > 0:
    dig = n % 10
    reverse = reverse * 10 + dig
    n = n // 10

if original_n == reverse:
    print("No. is a palindrome")
else:
    print("No. is not a palindrome")
