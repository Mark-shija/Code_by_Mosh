counts = {}
print("Enter your full name")
name = input("")
print("Enter your Education Specialization")
line = input("")

print("Let us count words from the text you provided")
words = line.split()
# Count the occurrences of each word
for word in words:
    counts[word] = counts.get(word, 0) + 1
    print("Counts", counts)

# Loop through the dictionary to check for "ICT" or "ict"
found = False
for key in counts:  # Loop through the keys of the dictionary
    if "ICT" in key.upper() or "ict" in key:  # Check if "ICT" or "ict" is in the key (case-insensitive)
        print(f"Congratulations, {name}, you have a specialization in ICT!")
        found = True
        break

if not found:
    print("Sorry, we don't have vacancies for you in the ICT field.")
