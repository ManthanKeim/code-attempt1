line = input("ENTER THE STRING :")
letters = {}

for i in line:
    if i in letters:
        letters[i] += 1
    else:
        letters[i] = 1

print(letters)

