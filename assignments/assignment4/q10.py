file_name = "practice.txt"

with open(file_name, "w", encoding="utf-8") as file:
    file.write("This is the first line.\n")

with open(file_name, "a", encoding="utf-8") as file:
    file.write("This line was appended.\n")

with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()

print(content)