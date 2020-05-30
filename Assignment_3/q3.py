# Frequency counter #
words = input("Enter your message:").lower()

counted = {}
keys = []
for items in words:
    if items not in keys:
        keys.append(items)

for key in set(words):
    counter = 0
    for letter in words:
        if key == letter:
            counter = counter + 1
    counted[key] = counter
print(counted)


