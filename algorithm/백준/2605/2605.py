# sol_1 - 문어박사 유튜브
students_num = int(input())
rule = list(map(int, input().split()))
line = [n for n in range(1, students_num + 1)]

for i in range(students_num):
    n, t = rule[i], line[i] # n: 몇 칸 앞으로, t: 해당 규칙을 적용시킬 학생 번호
    for j in range(i, i-n, -1):
        line[j] = line[j-1]
    line[i-n] = t

print(*line)