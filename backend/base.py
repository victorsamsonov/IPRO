from flask import Flask, request
import keras
import tensorflow
import numpy as np

api = Flask(__name__)

CLASS_MAP = {
    "CS 487": [13],
    "CS 440": [9],
    "MATH 251": [19],
    "CS 485": [12],
    "CS 351": [6],
    "CS 450": [10],
    "MATH 322": [21],
    "ELECT 2": [15],
    "MATH 151": [17],
    "CS 331": [3],
    "ELECT 3": [16],
    "ELECT 1": [14],
    "CS 340": [4],
    "MATH 152": [18],
    "CS 116": [1],
    "CS 430": [8],
    "CS 484": [11],
    "CS 350": [5],
    "CS 422": [7],
    "MATH 474": [22],
    "CS 330": [2],
    "CS 100":[0],
    "MATH 252": [20],
}

MEAN = 75.32247974384043
STD = 15
model = keras.models.load_model("my_model.h5")
# model.predict([0], [0.8])
@api.route('/predict', methods=["POST"])
def my_profile():
    print(request)
    data = request.json
    received_GPA = data.get("gpa")
    selected_class = data.get("class")
    mapped_class = CLASS_MAP[selected_class]
    processed_GPA = (float(received_GPA) / 4.0)
    input1 = np.array([[mapped_class]])
    input2 = np.array([[processed_GPA]])
    pred = model.predict([input1, input2])
    processed_pred = (pred * STD) + MEAN

    
    print(received_GPA)
    out = {"processed_pred":str(processed_pred[0][0])}
    return out

