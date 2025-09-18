s = input()

start = None
for i, ch in enumerate(s):
    if ch.isupper():
        start = i
        break

second = None
for i in range(len(s) - 1):
    if s[i].isdigit():
        second = i + 1
        break
        
step = second - start

result = ""
for i in range(start, len(s), step):
    result += s[i]
    if s[i] == ".":
        break

print(result)