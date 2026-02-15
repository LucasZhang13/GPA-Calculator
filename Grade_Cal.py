def rule(sum_credits, sum_grades):
    return sum_grades/sum_credits
print("请输入学分和成绩，输入End结束")
credits = []
grades = []
while True:
    _input = input()
    if _input.lower() == "end":
        break
    parts = _input.split()
    credit = int(parts[0])
    grade = int(parts[0]) * int(parts[1])
    credits.append(credit)
    grades.append(grade)
sum_credits = int(0)
sum_grades = int(0)
for credit in credits:
    sum_credits = sum_credits + credit
for grade in grades:
    sum_grades = sum_grades + grade
final_grades= int(rule(sum_credits, sum_grades))
score = final_grades
GPA = 0
if 90<=score<=100:
    GPA = 4.0
if 85<=score<90:
    GPA = 3.7
if 82<=score<85:
    GPA = 3.3
if 78<=score<82:
    GPA = 3.0
if 75<=score<78:
    GPA = 2.7
if 71<=score<75:
    GPA = 2.3
if 67<=score<71:
    GPA = 2.0
if 63<=score<67:
    GPA = 1.7
if 60<=score<63:
    GPA = 1.0
if 0<=score<60:
    GPA = 0.0
print("你的总学分为",sum_credits,"分", "加权平均成绩为",final_grades, "分", "GPA=", GPA)