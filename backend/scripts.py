import pandas as pd
import numpy as np
import random

N_STUDENTS = 1000
student_dict = {}
for i in range(1, N_STUDENTS+1):
    student_dict[f"Student_{i}"] = {}


def generate_gpa():
    while True:
        gpa = np.random.normal(loc=3.1, scale=0.5)  # Mean: 2.5, Standard Deviation: 1
        if 0 <= gpa <= 4.0:
            return round(gpa, 2)  # Round to two decimal places


def generate_grade(difficulty):
    while True:
        grade = np.random.normal(loc=70, scale=5)

        if 0 <= grade <= 100:
            return round(grade+difficulty, 2)  # Round to two decimal places


def generate_professor_difficulty():
    while True:
        difficulty = np.random.normal(loc=0, scale=10)
        if -25 <= difficulty <= 25: return round(difficulty, 2)  # Round to two decimal places


# Appending "GPA" key to each student's dictionary
for student in student_dict:
    gpa = generate_gpa()
    print(gpa)
    student_dict[student]["GPA"] = gpa



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
           "CS 422", "MATH 151", "MATH 152", "MATH 251", "MATH 322"]

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
professor_df_dict = {"PROFESSOR": [], "CLASS": [], "AVG": []} # Maybe include difficulty if needed
for professor in professor_dict:
    # print(professor)
    curr_prof = professor_dict[professor]
    for k in curr_prof["CLASSES"]:
        semester_class = curr_prof["CLASSES"][k]
        for c in semester_class:
            professor_df_dict["PROFESSOR"].append(professor)
            professor_df_dict["CLASS"].append(c[0])
            professor_df_dict["AVG"].append(c[1])



print(professor_df_dict)
pd.DataFrame(professor_df_dict).to_csv("professor_df.csv", index=False)



