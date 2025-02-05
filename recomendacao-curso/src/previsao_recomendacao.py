import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

ratings = pd.read_csv('../resources/datasets/ratings.csv')

students = ratings['UserID'].unique()
courses = ratings['Item'].unique()

student_to_index = {student: i for i, student in enumerate(students)}
course_to_index = {course: i for i, course in enumerate(courses)}

ratings['UserID'] = ratings['UserID'].map(student_to_index)
ratings['Item'] = ratings['Item'].map(course_to_index)

# Dividir treino e teste
train, test = train_test_split(ratings, test_size=0.2, random_state=42)

num_students = len(students)
num_courses = len(courses)
embedding_size = 8

student_input = keras.Input(shape=(1,), name="student")
course_input = keras.Input(shape=(1,), name="course")

student_embedding = layers.Embedding(num_students, embedding_size)(student_input)
course_embedding = layers.Embedding(num_courses, embedding_size)(course_input)

student_vector = layers.Flatten()(student_embedding)
course_vector = layers.Flatten()(course_embedding)

concat = layers.Concatenate()([student_vector, course_vector])
dense1 = layers.Dense(16, activation="relu")(concat)
dense2 = layers.Dense(8, activation="relu")(dense1)
output = layers.Dense(1)(dense2)  # Predição da nota do aluno para o curso

model = keras.Model([student_input, course_input], output)
model.compile(optimizer="adam", loss="mse", metrics=["mae"])

model.fit([train['UserID'], train['Item']], train['Rating'], epochs=10, batch_size=32)

def prever(estudante, curso):
    student_idx = student_to_index.get(estudante, None)
    course_idx = course_to_index.get(curso, None)

    if student_idx is None or course_idx is None:
        return 0

    student_input = np.array([[student_idx]])
    course_input = np.array([[course_idx]])

    return model.predict({"student": student_input, "course": course_input}, verbose=0)[0][0]