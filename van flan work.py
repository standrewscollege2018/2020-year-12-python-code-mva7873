# manage student info about level 1 ncea creadts 
# max v.l
# 11/2/2020

students = ["max", "garry", "sharon", "poppy"]
#desplay all students
for index in range(0, len(students)):
    print(index+1, students[index])
    
print("what student do you wish to terminate")
print("sleact the number of the student")

n = int(input())
del students[n]
#desplay all students
for index in range(0, len(students)):
    print(index+1, students[index])

