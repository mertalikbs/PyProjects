student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    check = student_scores[student]
    if check >= 91 and check <= 100:
        student_grades[student] = "Outstanding"
    elif check <= 90 and check >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif check <= 80 and check >= 71:
        student_grades[student] = "Acceptable"
    elif check <= 70:
        student_grades[student] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades)