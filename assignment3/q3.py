input_1 = input("Enter the number: ")
reverse_input = input_1[::-1]

if(input_1 == reverse_input):
    print("They are palindrome")
else:
    print("They aren't palindrome")