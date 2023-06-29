# spisok = [1, 56, 78, 19, 17, 91, 64, -16]
spisok = ["apple", "six", "box"]
a = spisok[0]
for ch in spisok:
    if len(ch) > len(a):
        a = ch
print(a)