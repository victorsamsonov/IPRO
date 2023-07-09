import pandas as pd
import numpy as np

N_STUDENTS = 1000
student_dict = {}
for i in range(1, N_STUDENTS+1):
    student_dict[f"Student_{i}"] = {}


def generate_gpa():
    while True:
        gpa = np.random.normal(loc=3.1, scale=0.5)  # Mean: 2.5, Standard Deviation: 1
        if 0 <= gpa <= 4.0:
            return round(gpa, 2)  # Round to two decimal places

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

df_dict, df = dict_to_df()
df.to_csv("Dataframe.csv", index=False)

