import csv
Y=[]
X=[]
gender=[]
ev_mar=[]
work_type=[]
res_type=[]
smo_stat=[]
# Open the CSV file
file_path = "healthcare-dataset-stroke-data.csv"
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)

    # Skip the header row (if needed)
    header = next(csv_reader)
    # prfloat("Header:", header)

    # Read and print each row
    for row in csv_reader:
        Y.append(float(row[11]))
        r=[]
        if row[1]  not in gender:
            gender.append(row[1])
        r.append(gender.index(row[1]))

        r.append(float(row[2]))
        r.append(float(row[3]))
        r.append(float(row[4]))
        if row[5] not in ev_mar:
            ev_mar.append(row[5])
        r.append(ev_mar.index(row[5]))
        if row[6] not in work_type:
            work_type.append(row[6])
        r.append(work_type.index(row[6]))
        if row[7] not in res_type:
            res_type.append(row[7])
        r.append(res_type.index(row[7]))
        r.append(float(row[8]))
        r.append(float(row[9]))

        if row[10] not in smo_stat:
            smo_stat.append(row[10])
        r.append(smo_stat.index(row[10]))
        X.append(r)
        print(row)


print(len(X))
print(len(Y))
print(X[0])
print(Y[0])


# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

from imblearn.over_sampling import SMOTE
sm = SMOTE(random_state = 2)
print(len(X))
X_train_res, y_train_res = sm.fit_resample(X, Y)
print(len(X_train_res))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_train_res, y_train_res, test_size=0.2, random_state=42)

# Create a Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Make predictions
y_pred = rf_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))
