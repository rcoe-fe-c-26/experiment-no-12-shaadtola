# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder: Shaad Tola
# Date: 9-2-26

print("--- Extracting Words from Text File ---\n")
num = int(input("Enter Length of Words: "))
result = []

with open("story.txt", "r") as f:
    content = f.read().lower().split()

for i in content:
    if len(i) == num:
        result.append(i)

final = sorted(set(result))

print(f"Words with length {num} are:", final)


