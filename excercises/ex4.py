#Ex-4. Need numbers
#A crazy trainer returns my grade into single string and I need to know the total and the average
# "English=68 Logic=75 Uml=87 Code=80"
string_grade="English=68 Logic=75 Uml=87 Code=80"
list_grade=string_grade.split()
sum=0
average=0
for course in list_grade:
    note=course.split("=")
    sum+=int(note[1])

print(f"The total sum is: {sum}")
print(f"The average is: {sum/len(list_grade)}")