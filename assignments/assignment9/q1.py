import re


samples = {
    "emails": ["test.user@example.com", "bad-email@", "hello123@gmail.com"],
    "mobile_numbers": ["9876543210", "+91-9876543210", "12345"],
    "strings": ["HelloWorld", "hello world", "Python123"],
    "urls": ["https://example.com", "http://site.org/page", "not-a-url"],
    "passwords": ["Pass@123", "weakpass", "Admin#2026"],
}


patterns = {
    "email": re.compile(r"^[\w.+-]+@[\w-]+\.[\w.-]+$"),
    "mobile": re.compile(r"^(?:\+\d{1,3}[- ]?)?\d{10}$"),
    "alpha_string": re.compile(r"^[A-Za-z]+$"),
    "url": re.compile(r"^https?://[\w.-]+(?:/[\w./-]*)?$"),
    "password": re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$"),
}


def test_pattern(label, pattern, values):
    print(label)
    for value in values:
        print(f"{value!r} -> {bool(pattern.match(value))}")
    print()


test_pattern("Email validation", patterns["email"], samples["emails"])
test_pattern("Mobile number validation", patterns["mobile"], samples["mobile_numbers"])
test_pattern("Alphabetic string validation", patterns["alpha_string"], samples["strings"])
test_pattern("URL validation", patterns["url"], samples["urls"])
test_pattern("Password validation", patterns["password"], samples["passwords"])

text = "Python 3.13 is great!"
print("Find words in a sentence:")
print(re.findall(r"\b\w+\b", text))