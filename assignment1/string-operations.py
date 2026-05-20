str1 = "Hello"
str2 = "world"

#performing concatenation
str3 = str1 + str2
print(str3)

#performing uppercase and lowercase on string(str2)
print(str2.upper())
print(str2.lower())

#performing title and swapcase on string(str3)
str3 = str3.lower()
#first converted str3 to lower for better understanding of "title()"
print(str3.title())
print(str3.swapcase())

#performing capitalize on string(str3)
print(str3.capitalize())

#performing casefold on string(str3)
print(str3.casefold())

#performing center on string(str3)
print(str3.center(69))

#performing count on string(str3)
print(str3.count("l"))

#performing endswith and find on string(str3)
print(str3.endswith("world"))
print(str3.find("hello"))

#performing isalnum, isdigit, isnumeric, and isspace on string(str3)
print(str3.isalnum())
print(str3.isdigit())
print(str3.isnumeric())
print(str3.isspace())

#performing replace on string(str3)
print(str3.replace("world", "python"))