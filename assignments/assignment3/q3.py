number = int(input("Enter a number: "))

temp = number
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if number == reverse:
    print(number, "is a Palindrome Number")
else:
    print(number, "is not a Palindrome Number")