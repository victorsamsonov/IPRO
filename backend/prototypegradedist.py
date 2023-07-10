"""
import matplotlib.pyplot as plt
import numpy as np

ages=[22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]

plt.hist(ages, bins=5, histtype="bar", rwidth=0.8)
plt.show()
"""

import pandas as pd
import matplotlib.pyplot as plt

ClassName = input("Enter the class name: ")

df = pd.read_csv("C:/Users/danis/Downloads/Gradedistproto.csv") 

selected_class = df[df['Class'] == ClassName]

if selected_class.empty:
    print(f"No data for class {ClassName}")
else:
    # Get the grades only, ignoring the class column
    grades = selected_class.iloc[0, 1:]

    # Normalize the values to get percentages
    grades_percentage = grades / grades.sum() * 100

    plt.bar(grades_percentage.index, grades_percentage.values)
    plt.title('Grade Distribution')
    plt.xlabel('Grade')
    plt.ylabel('Percentage')
    plt.show()
