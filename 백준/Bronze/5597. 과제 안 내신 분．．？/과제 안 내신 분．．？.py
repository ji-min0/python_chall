students = set(range(1,31))
submitted_students = {int(input()) for i in range(28)}

not_submitted = set.difference(students, submitted_students)

for n in sorted(not_submitted): 
    print(n)