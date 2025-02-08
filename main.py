import random
newl = []
rang = input("Enter a number: ")
for i in range(int(rang)):
    el = random.randint(1048, 1104)
    if el in newl:
        break
    else: newl.append(chr(el))
print("".join(newl))

































