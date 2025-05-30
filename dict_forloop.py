# for key, value in my_dict.items():
#     print(f"Key: {key}, Value: {value}")

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={
}
for key, value in student_scores.items():
    if value >= 91 and value <= 100:
        grade = "Outstanding"
    elif value >= 81 and value <= 90:
        grade = "Exceeds Expectations"
    elif value >= 71 and value <= 80:
        grade = "Acceptable"
    elif value <= 70:
        grade = "Fail"    
    student_grades[key] = grade

print(student_grades)    
         