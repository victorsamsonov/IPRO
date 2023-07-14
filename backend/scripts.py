import pandas as pd
import numpy as np
import random

N_STUDENTS = 1000
student_dict = {}
for i in range(1, N_STUDENTS+1):
    student_dict[f"Student_{i}"] = {}

def generate_grades2(num_students, avg_grade):
    total_points = num_students * avg_grade
    grade_dict = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    while total_points > 0:
        print(total_points)

        student_grade = np.random.normal(loc=avg_grade, scale=avg_grade*.2)
        if student_grade > 100:
            student_grade = 100
        elif student_grade < 0:
            student_grade = 0
        if (total_points - student_grade) > 0 and total_points >= 60:
            print("yee")
            if student_grade >= 90:
                grade_dict["A"] += 1
            elif student_grade >= 80:
                grade_dict["B"] += 1
            elif student_grade >= 70:
                grade_dict["C"] += 1
            elif student_grade >= 60:
                grade_dict["D"] += 1
            elif student_grade < 60:
                grade_dict["E"] += 1
            total_points -= student_grade
        else:
            print('yo')
            student_grade = total_points
            if student_grade >= 90:
                grade_dict["A"] += 1
            elif student_grade >= 80:
                grade_dict["B"] += 1
            elif student_grade >= 70:
                grade_dict["C"] += 1
            elif student_grade >= 60:
                grade_dict["D"] += 1
            elif student_grade < 60:
                grade_dict["E"] += 1
            total_points = 0
    return grade_dict

def generate_grades(num_students, avg_grade):
    total_points = avg_grade * num_students
    grade_weights = [90, 80, 70, 60, 50]  # Adjust the weights as needed
    # student

    # Generate grades
    grades = []
    remaining_students = num_students
    for i, weight in enumerate(grade_weights):
        num = int(weight / sum(grade_weights) * num_students)
        grades.append(num)
        remaining_students -= num
    print(grades)
    # Distribute the remaining students
    while remaining_students > 0:
        idx = random.randint(0, len(grades) - 1)
        grades[idx] += 1
        remaining_students -= 1

    grade_dict = {'A': grades[0], 'B': grades[1], 'C': grades[2], 'D': grades[3], 'E': grades[4]}
    return grade_dict
def generate_gpa():
    while True:
        gpa = np.random.normal(loc=3.1, scale=0.5)  # Mean: 2.5, Standard Deviation: 1
        if 0 <= gpa <= 4.0:
            return round(gpa, 2)  # Round to two decimal places


def generate_grade(difficulty):
    while True:
        grade = np.random.normal(loc=70, scale=5)

        if 0 <= grade+difficulty <= 100:
            return round(grade+difficulty, 2)  # Round to two decimal places


def generate_professor_difficulty():
    while True:
        difficulty = np.random.normal(loc=0, scale=10)
        if -25 <= difficulty <= 25: return round(difficulty, 2)  # Round to two decimal places
GPA_SUM = 0

# Appending "GPA" key to each student's dictionary
for student in student_dict:
    gpa = generate_gpa()
    print(gpa)
    student_dict[student]["GPA"] = gpa
    GPA_SUM += gpa


for student in student_dict:
    student_dict[student]["GPA_PROB"] = student_dict[student]["GPA"] / GPA_SUM

COLUMNS = ["GPA"]
def dict_to_df():
    df_dict = {"STUDENTS":[]}
    for c in COLUMNS: df_dict[c] = []
    for k in student_dict:
        df_dict["STUDENTS"].append(k)
        for c in COLUMNS:
            df_dict[c].append(student_dict[k][c])
    df = pd.DataFrame(df_dict)
    return df_dict, df


N_SEMESTERS = 3 
CLASSES = ["CS 100", "CS 116", "CS 350", "CS 450", "CS 351", "CS 340", "CS 440", "CS 430", "CS 485", "CS 487", "CS 484",
           "CS 422", "MATH 151", "MATH 152", "MATH 251", "MATH 322", "MATH 252", "CS 331", "CS 330", "MATH 474"]

professor_dict = {}

for i in range(10):
    professor_dict[f"Professor_{i}"] = {}
    professor_dict[f"Professor_{i}"]["CLASSES"] = {s+1: [] for s in range(N_SEMESTERS)}
    print("Difficulty")
    diff = generate_professor_difficulty()
    print(diff)
    professor_dict[f"Professor_{i}"]["DIFFICULTY"] = diff
available_classes = CLASSES.copy()

for k in professor_dict:
    difficulty = professor_dict[k]["DIFFICULTY"]
    n_choices = random.randint(1, 3)
    for i in range(n_choices):
        if available_classes:
            choice = random.choice(available_classes)
            available_classes.remove(choice)
            for s in professor_dict[k]['CLASSES']:
                professor_dict[k]['CLASSES'][s].append((choice, generate_grade(difficulty)))

print(professor_dict)
df_dict, df = dict_to_df()
df.to_csv("Dataframe.csv", index=False)
# use to create a final df
professor_df_dict = {"PROFESSOR": [], "CLASS": [], "AVG": [], "N_STUDENTS": [], "A": [], "B": [], "C": [], "D": [], "E": []}  # Maybe include difficulty if needed
for professor in professor_dict:
    # print(professor)
    curr_prof = professor_dict[professor]
    for k in curr_prof["CLASSES"]:
        semester_class = curr_prof["CLASSES"][k]
        for c in semester_class:
            n_students = random.randint(20, 120)
            professor_df_dict["PROFESSOR"].append(professor)
            professor_df_dict["CLASS"].append(c[0])
            professor_df_dict["AVG"].append(c[1])
            professor_df_dict["N_STUDENTS"].append(n_students)
            grade_df = generate_grades2(n_students, c[1])
            for k in grade_df:
                professor_df_dict[k].append(grade_df[k])

print(professor_df_dict)
pd.DataFrame(professor_df_dict).to_csv("professor_df.csv", index=False)
print(generate_grades2(2, 40))
print(GPA_SUM)




