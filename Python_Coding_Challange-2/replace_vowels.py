text = input("Enter String: ")
result = ""

for char in text:
    if char.lower() in "aeiou":
        result += "*"  # Add a star if it's a vowel
    else:
        result += char # Add the original letter if it's not
        
print(result)
