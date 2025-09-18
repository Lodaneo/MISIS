N = int(input())

очные = 0
заочные = 0

for _ in range(N):
    фамилия, имя, возраст, формат = input().split()
    if формат == "True":
        очные += 1
    else:
        заочные += 1

print(очные,заочные)