import pandas as pd
import numpy as np
import random

N_STUDENTS = 1000
student_dict = {}
for i in range(1, N_STUDENTS+1):
    student_dict[f"Student_{i}"] = {}


def generate_grades2(num_students, avg_grade, student_df, class_name, curr_semester):
    total_points = num_students * avg_grade
    grade_dict = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    gpa_list = student_df["GPA"]
    shifted_gpa = (gpa_list - AVG_GPA).values
    student_grades = []

    idx = 0
    while total_points > 0 and idx < num_students:

        student_grade = np.random.normal(loc=avg_grade, scale=avg_grade*.2)
        if student_grade > 100:
            student_grade = 100
        elif student_grade < 0:
            student_grade = 0
        student_grade = min(max(avg_grade + ((shifted_gpa[idx]/4.0)*avg_grade), 0), 100)
        student_grades.append(student_grade)
        if (total_points - student_grade) > 0 and total_points >= 60:

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
        idx += 1
    while idx < num_students:
        grade_dict["E"] += 1
        student_grades.append(avg_grade)
        idx += 1
    # print(idx)
    print(student_df)
    student_df["CLASS"] = class_name
    print(len(student_df), len(student_grades), num_students, idx)
    student_df["GRADE"] = student_grades[:len(student_df["GRADE"].values)]
    student_df["SEMESTER"] = curr_semester

    return grade_dict, student_df


AVG_GPA = 3.1


def generate_gpa():
    while True:
        gpa = np.random.normal(loc=AVG_GPA, scale=0.4)
        if 0 <= gpa+0.2 <= 4.0:
            return round(gpa+0.2, 2)  # Round to two decimal places


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

COLUMNS = ["GPA", "GPA_PROB"]
def dict_to_df():
    df_dict = {"STUDENTS":[]}
    for c in COLUMNS: df_dict[c] = []
    for k in student_dict:
        df_dict["STUDENTS"].append(k)
        for c in COLUMNS:
            print(c)
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
    # print("Difficulty")
    diff = generate_professor_difficulty()
    # print(diff)
    professor_dict[f"Professor_{i}"]["DIFFICULTY"] = diff
available_classes = CLASSES.copy()

semester_mapping = {1: "Fall 2022", 2: "Spring 2023", 3: "Fall 2023"}
for k in professor_dict:
    difficulty = professor_dict[k]["DIFFICULTY"]
    n_choices = random.randint(1, 3)
    for i in range(n_choices):
        if available_classes:
            choice = random.choice(available_classes)
            available_classes.remove(choice)
            for s in professor_dict[k]['CLASSES']:
                professor_dict[k]['CLASSES'][s].append((choice, generate_grade(difficulty)))

# print(professor_dict)
df_dict, df = dict_to_df()
df["CLASS"] = None
df["GRADE"] = 70.0
df["SEMESTER"] = ""
df.to_csv("Students.csv", index=False)
# use to create a final df
new_df = df.copy()
professor_df_dict = {"PROFESSOR": [], "SEMESTER": [], "CLASS": [], "AVG": [], "N_STUDENTS": [], "A": [], "B": [], "C": [], "D": [], "E": []}  # Maybe include difficulty if needed
for professor in professor_dict:
    curr_student_idx = 0
    # print(professor)
    curr_prof = professor_dict[professor]
    for curr_semester in curr_prof["CLASSES"]:
        print("THE K")
        print(k)
        semester_class = curr_prof["CLASSES"][curr_semester]
        for c in semester_class:
            n_students = random.randint(20, 120)
            professor_df_dict["PROFESSOR"].append(professor)
            professor_df_dict["CLASS"].append(c[0])
            print(k)
            print(semester_mapping[curr_semester])
            professor_df_dict["SEMESTER"].append(semester_mapping[curr_semester])
            professor_df_dict["AVG"].append(c[1])
            professor_df_dict["N_STUDENTS"].append(n_students)
            if curr_student_idx+n_students > N_STUDENTS:curr_student_idx = 0
            grade_df, updated_df = generate_grades2(n_students, c[1], df.iloc[curr_student_idx:curr_student_idx+n_students,], c[0], semester_mapping[curr_semester])
            # df.iloc[curr_student_idx:curr_student_idx + n_students,] = updated_df
            new_df = pd.concat([new_df, updated_df])
            curr_student_idx += n_students
            if curr_student_idx > N_STUDENTS: curr_student_idx
            for k in grade_df:
                professor_df_dict[k].append(grade_df[k])

print(professor_df_dict)
pd.DataFrame(professor_df_dict).to_csv("professor_df.csv", index=False)

print(GPA_SUM)
print(df)
print(new_df.iloc[1000:,])
new_df = new_df.iloc[1000:,]
new_df.to_csv("updated_student_grades2.csv")
print('yo')




