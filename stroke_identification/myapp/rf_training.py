# import csv
# Y=[]
# X=[]
# gender=[]
# ev_mar=[]
# work_type=[]
# res_type=[]
# smo_stat=[]
# # Open the CSV file
# file_path = r"C:\Users\kshiv\PycharmProjects\stroke_identification\myapp\healthcare-dataset-stroke-data.csv"
# with open(file_path, mode='r') as file:
#     csv_reader = csv.reader(file)
#
#     # Skip the header row (if needed)
#     header = next(csv_reader)
#     # prfloat("Header:", header)
#
#     # Read and print each row
#     for row in csv_reader:
#         Y.append(float(row[11]))
#         r=[]
#         if row[1]  not in gender:
#             gender.append(row[1])
#         r.append(gender.index(row[1]))
#
#         r.append(float(row[2]))
#         r.append(float(row[3]))
#         r.append(float(row[4]))
#         if row[5] not in ev_mar:
#             ev_mar.append(row[5])
#         r.append(ev_mar.index(row[5]))
#         if row[6] not in work_type:
#             work_type.append(row[6])
#         r.append(work_type.index(row[6]))
#         if row[7] not in res_type:
#             res_type.append(row[7])
#         r.append(res_type.index(row[7]))
#         r.append(float(row[8]))
#         r.append(float(row[9]))
#
#         if row[10] not in smo_stat:
#             smo_stat.append(row[10])
#         r.append(smo_stat.index(row[10]))
#         X.append(r)
#         print(row)
#
# print(gender)
# print(work_type)
# print(res_type)
# print(smo_stat)
# print(len(X))
# print(len(Y))
# print(X[0])
# print(Y[0])
#
#
# # Import necessary libraries
# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, classification_report
#
# from imblearn.over_sampling import SMOTE
# sm = SMOTE(random_state = 2)
# print(len(X))
# X_train_res, y_train_res = sm.fit_resample(X, Y)
# print(len(X_train_res))
#
# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X_train_res, y_train_res, test_size=0.2, random_state=42)
#
# # Create a Random Forest Classifier
# rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
#
# # Train the model
# rf_model.fit(X_train_res, y_train_res)
#
# # Make predictions
# y_pred = rf_model.predict(X_test)
# for i in range(len(y_pred)):
#     if y_pred[i]==1:
#         print("*****************")
#         print(X_test[i])
# # Evaluate the model
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Accuracy: {accuracy:.2f}")
# print("\nClassification Report:\n", classification_report(y_test, y_pred))
#
#
#
# def predict_rf_fn(row):
#     print("++++++++++1111111111111111111")
#     print(row)
#     return rf_model.predict([row])[0]
# import csv
# Y=[]
# X=[]
# gender=[]
# ev_mar=[]
# work_type=[]
# res_type=[]
# smo_stat=[]
# # Open the CSV file
# file_path = r"C:\Users\kshiv\PycharmProjects\stroke_identification\myapp\healthcare-dataset-stroke-data.csv"
# with open(file_path, mode='r') as file:
#     csv_reader = csv.reader(file)
#
#     # Skip the header row (if needed)
#     header = next(csv_reader)
#     # prfloat("Header:", header)
#
#     # Read and print each row
#     for row in csv_reader:
#         Y.append(float(row[11]))
#         r=[]
#         if row[1]  not in gender:
#             gender.append(row[1])
#         r.append(gender.index(row[1]))
#
#         r.append(float(row[2]))
#         r.append(float(row[3]))
#         r.append(float(row[4]))
#         if row[5] not in ev_mar:
#             ev_mar.append(row[5])
#         r.append(ev_mar.index(row[5]))
#         if row[6] not in work_type:
#             work_type.append(row[6])
#         r.append(work_type.index(row[6]))
#         if row[7] not in res_type:
#             res_type.append(row[7])
#         r.append(res_type.index(row[7]))
#         r.append(float(row[8]))
#         r.append(float(row[9]))
#
#         if row[10] not in smo_stat:
#             smo_stat.append(row[10])
#         r.append(smo_stat.index(row[10]))
#         X.append(r)
#         print(row)
#
# print(gender)
# print(work_type)
# print(res_type)
# print(smo_stat)
# print(len(X))
# print(len(Y))
# print(X[0])
# print(Y[0])
#
#
# # Import necessary libraries
# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, classification_report
#
#
# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
#
# # Create a Random Forest Classifier
# rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
#
# # Train the model
# rf_model.fit(X_train, y_train)
#
# # Make predictions
# y_pred = rf_model.predict(X_test)
# for i in range(len(y_pred)):
#      if y_pred[i]==1:
#         print("*****************")
#         print(X_test[i])
#
# # Evaluate the model
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Accuracy: {accuracy:.2f}")
# print("\nClassification Report:\n", classification_report(y_test, y_pred))
#
#
# def predict_rf_fn(row):
#     print("++++++++++1111111111111111111")
#     print(row)
#     return rf_model.predict([row])[0]
# import csv
# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, classification_report
# from imblearn.over_sampling import SMOTENC
# from sklearn.preprocessing import OneHotEncoder
#
# # Initialize lists
# Y = []
# X = []
# gender = []
# ev_mar = []
# work_type = []
# res_type = []
# smo_stat = []
#
# # File path to dataset
# file_path = r"C:\Users\kshiv\PycharmProjects\stroke_identification\myapp\healthcare-dataset-stroke-data.csv"
#
# # Open the CSV file
# with open(file_path, mode='r') as file:
#     csv_reader = csv.reader(file)
#     header = next(csv_reader)  # Skip the header row
#
#     # Read each row
#     for row in csv_reader:
#         Y.append(float(row[11]))  # Target variable
#
#         r = []
#         # Collect categorical feature values for encoding
#         gender.append(row[1])
#         ev_mar.append(row[5])
#         work_type.append(row[6])
#         res_type.append(row[7])
#         smo_stat.append(row[10])
#
#         r.append(float(row[2]))  # Age
#         r.append(float(row[3]))  # Hypertension
#         r.append(float(row[4]))  # Heart Disease
#         r.append(float(row[8]))  # Average Glucose Level
#         r.append(float(row[9]))  # BMI
#
#         X.append(r)
#
# # Convert categorical features to numpy arrays for encoding
# gender = np.array(gender).reshape(-1, 1)
# ev_mar = np.array(ev_mar).reshape(-1, 1)
# work_type = np.array(work_type).reshape(-1, 1)
# res_type = np.array(res_type).reshape(-1, 1)
# smo_stat = np.array(smo_stat).reshape(-1, 1)
#
# # Apply One-Hot Encoding to categorical features
# encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
# encoded_gender = encoder.fit_transform(gender)
# encoded_ev_mar = encoder.fit_transform(ev_mar)
# encoded_work_type = encoder.fit_transform(work_type)
# encoded_res_type = encoder.fit_transform(res_type)
# encoded_smo_stat = encoder.fit_transform(smo_stat)
#
# # Concatenate encoded categorical features with numerical features
# X_encoded = np.hstack((encoded_gender, encoded_ev_mar, encoded_work_type, encoded_res_type, encoded_smo_stat, X))
#
# # Define categorical feature indices after One-Hot Encoding
# categorical_features = list(range(encoded_gender.shape[1] +
#                                   encoded_ev_mar.shape[1] +
#                                   encoded_work_type.shape[1] +
#                                   encoded_res_type.shape[1] +
#                                   encoded_smo_stat.shape[1]))
#
# # Apply SMOTENC to handle categorical variables properly
# sm = SMOTENC(categorical_features=categorical_features, random_state=2)
# X_resampled, Y_resampled = sm.fit_resample(X_encoded, Y)
#
# print("Resampled Dataset Size: ", len(X_resampled))
#
# # Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X_resampled, Y_resampled, test_size=0.2, random_state=42)
#
# # Create a Random Forest Classifier with improved hyperparameters
# rf_model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
#
# # Train the model
# rf_model.fit(X_train, y_train)
#
# # Make predictions
# y_pred = rf_model.predict(X_test)
#
# # Print samples where prediction is 1 (Stroke detected)
# for i in range(len(y_pred)):
#     if y_pred[i] == 1:
#         print("*****************")
#         print(np.round(X_test[i], 2))  # Rounding values for readability
#
# # Evaluate the model
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Accuracy: {accuracy:.2f}")
# print("\nClassification Report:\n", classification_report(y_test, y_pred))
#
#
# # Prediction function using the trained model
# def predict_rf_fn(gender_input, ev_mar_input, work_type_input, res_type_input, smo_stat_input, age, hypertension,
#                   heart_disease, glucose, bmi):
#     # Encode categorical inputs
#     input_data = np.array([[gender_input, ev_mar_input, work_type_input, res_type_input, smo_stat_input]])
#     encoded_input = encoder.transform(input_data)  # One-Hot Encoding
#
#     # Convert to numerical array and concatenate
#     feature_vector = np.hstack((encoded_input, [[age, hypertension, heart_disease, glucose, bmi]]))
#
#     # Ensure correct shape
#     feature_vector = feature_vector.reshape(1, -1)
#
#     # Predict and round the result
#     prediction = rf_model.predict(feature_vector)[0]
#
#     print("++++++++++ Prediction Input ++++++++++")
#     print(np.round(feature_vector, 2))  # Round for readability
#
#     return int(prediction)  # Return as an integer (0 or 1)

# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.preprocessing import LabelEncoder
# from imblearn.over_sampling import SMOTENC
#
# # Load dataset
# file_path = r"C:\Users\kshiv\PycharmProjects\stroke_identification\myapp\healthcare-dataset-stroke-data.csv"
# df = pd.read_csv(file_path)
#
# # Drop rows with missing values (e.g., bmi)
# df = df.dropna()
#
# # Encode categorical features using LabelEncoder
# categorical_cols = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
# encoders = {}
# for col in categorical_cols:
#     le = LabelEncoder()
#     df[col] = le.fit_transform(df[col])
#     encoders[col] = le  # Save encoders if needed later
#
# # Define features and target
# X = df.drop(['stroke', 'id'], axis=1)
# Y = df['stroke']
#
# # Specify categorical feature indices for SMOTENC
# categorical_feature_indices = [X.columns.get_loc(col) for col in categorical_cols]
#
# # Apply SMOTENC to balance the dataset
# smote_nc = SMOTENC(categorical_features=categorical_feature_indices, random_state=42)
# X_resampled, Y_resampled = smote_nc.fit_resample(X, Y)
#
# # Convert to DataFrame for rounding
# X_resampled_df = pd.DataFrame(X_resampled, columns=X.columns)
#
# # Round only relevant columns
# X_resampled_df["age"] = X_resampled_df["age"].round(0).astype(int)  # Age should be integer
# X_resampled_df["avg_glucose_level"] = X_resampled_df["avg_glucose_level"].round(1)
# X_resampled_df["bmi"] = X_resampled_df["bmi"].round(1)
#
# # Update X_resampled with cleaned values
# X_resampled = X_resampled_df
#
# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(X_resampled, Y_resampled, test_size=0.2, random_state=42)
#
# # Train the Random Forest model
# rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
# rf_model.fit(X_train, y_train)
#
# # Predictions
# y_pred = rf_model.predict(X_test)
#
# # Print samples predicted as stroke-positive
# for i in range(len(y_pred)):
#     if y_pred[i] == 0:
#         print("*****************")
#         print(X_test.iloc[i].tolist())
#
# # Evaluation
# accuracy = accuracy_score(y_test, y_pred)
# print(f"\nAccuracy: {accuracy:.2f}")
# print("\nClassification Report:\n", classification_report(y_test, y_pred))
# def siviarity(rowss):
#     import csv
#
#     Y = []
#     X = []
#     gender = []
#     ev_mar = []
#     work_type = []
#     res_type = []
#     smo_stat = []
#
#     # File path to dataset
#     file_path = r"C:\Users\kshiv\PycharmProjects\stroke_identification\myapp\stroke_dataset_with_45_high_severity_gender_fixed.csv"
#
#     # Open the CSV file
#     with open(file_path, mode='r') as file:
#         csv_reader = csv.reader(file)
#         header = next(csv_reader)  # Skip the header row
#         sim=10000000
#         op=""
#         # Read each row
#         for row in csv_reader:
#             # Y.append(float(row[12]))  # Target variable
#
#             r = []
#
#             gender.append(row[1])
#             ev_mar.append(row[5])
#             work_type.append(row[6])
#             res_type.append(row[7])
#             smo_stat.append(row[10])
#
#             r.append(float(row[2]))  # Age
#             r.append(float(row[3]))  # Hypertension
#             r.append(float(row[4]))  # Heart Disease
#             r.append(float(row[8]))  # Average Glucose Level
#             r.append(float(row[9]))  # BMI
#
#             import math
#             vec1 = [1, 2, 3]
#             vec2 = [1, 2, 3]
#             if int(row[11])==1:
#
#             # Euclidean distance
#                 distance = math.sqrt(sum((float(a) - float(b)) ** 2 for a, b in zip(row, r)))
#                 print(distance,"====================")
#                 print(distance,"====================")
#                 print(distance,"====================")
#
#                 if distance<sim:
#                     sim =distance
#                     op=row[12]
#         return op
#             #
# # Function to predict on a single row
# # def predict_rf_fn(row):
# #     op="Normal"
# #     res=rf_model.predict([row])[0]
# #     print(res)
# #     print("++++++++===============")
# #     print("++++++++===============")
# #     print("++++++++===============")
# #     if res==1:
# #         op=siviarity(row)
# #     return rf_model.predict([row])[0],op
# # print("((((((((((((((((((((((((()))))))))))))))))))))))))")
# def predict_rf_fn(full_row):
#     res = rf_model.predict([full_row])[0]
#     if res == 1:
#         # Extract only the 5 required features in order:
#         row_for_severity = [
#             full_row[1],  # age
#             full_row[2],  # hypertension
#             full_row[3],  # heart_disease
#             full_row[7],  # avg_glucose_level
#             full_row[8]  # bmi
#         ]
#         severity = siviarity(row_for_severity)
#         print("Severity Level:", severity)
#     else:
#         severity = "Normal"
#         print("Severity Level:", severity)
#     return res, severity
# the ordinsaal
#
            # print(predict_rf_fn([0,	65,	1,	1,	1,	1,	1,	194	,34	,2]))
# !iriguinal import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.preprocessing import LabelEncoder
# from imblearn.over_sampling import SMOTENC
# from scipy.spatial.distance import cdist
#
# # Load dataset
# file_path = r"C:\Users\kshiv\PycharmProjects\stroke_identification\myapp\healthcare-dataset-stroke-data.csv"
# df = pd.read_csv(file_path)
#
# # Drop rows with missing values
# df = df.dropna()
#
# # Encode categorical features
# categorical_cols = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
# encoders = {}
# for col in categorical_cols:
#     le = LabelEncoder()
#     df[col] = le.fit_transform(df[col])
#     encoders[col] = le  # Save encoders for decoding or new data
#
# # Print how each category was encoded
# print("\n=== Label Encoding Mapping ===")
# for col in encoders:
#     print(f"{col} encoding: {dict(zip(encoders[col].classes_, encoders[col].transform(encoders[col].classes_)))}")
#
# # Define features and target
# X = df.drop(['stroke', 'id'], axis=1)
# Y = df['stroke']
#
# # Get indices for categorical features
# categorical_feature_indices = [X.columns.get_loc(col) for col in categorical_cols]
#
# # Apply SMOTENC to handle imbalance
# smote_nc = SMOTENC(categorical_features=categorical_feature_indices, random_state=42)
# X_resampled, Y_resampled = smote_nc.fit_resample(X, Y)
#
# # Create DataFrame
# X_resampled_df = pd.DataFrame(X_resampled, columns=X.columns)
#
# # Round numerical features
# X_resampled_df["age"] = X_resampled_df["age"].round(0).astype(int)
# X_resampled_df["avg_glucose_level"] = X_resampled_df["avg_glucose_level"].round(1)
# X_resampled_df["bmi"] = X_resampled_df["bmi"].round(1)
#
# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(
#     X_resampled_df, Y_resampled, test_size=0.2, random_state=42
# )
#
# # Train Random Forest
# rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
# rf_model.fit(X_train, y_train)
#
# # For severity calculation
# stroke_positive_train_data = X_train[y_train == 1].reset_index(drop=True)
#
# # Evaluate model
# y_pred = rf_model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f"\nAccuracy: {accuracy:.2f}")
# print("\nClassification Report:\n", classification_report(y_test, y_pred))
#
# # Print stroke-positive samples
# for i in range(len(y_pred)):
#     if y_pred[i] == 1:
#         print("*****************")
#         print(X_test.iloc[i].tolist())
#
# # Predict stroke class (0/1)
# def predict_rf_fn(row):
#     return rf_model.predict([row])[0]
#
# # Predict stroke + severity
# def predict_stroke_and_severity(row):
#     prediction = rf_model.predict([row])[0]
#
#     if prediction == 0:
#         return "Normal", "None"
#
#     # Compute distance to stroke-positive cases
#     distances = cdist([row], stroke_positive_train_data, metric='euclidean')
#     min_dist = np.min(distances)
#     print("Prediction: Stroke, Distance to closest stroke-positive:", min_dist)
#     # Define severity level
#     if min_dist <= 5:
#         severity = "High"
#     elif min_dist <= 10:
#         severity = "Moderate"
#     else:
#         severity = "Mild"
#
#     return "Stroke", severity end original
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTENC

# Load dataset
file_path = r"C:\Users\kshiv\PycharmProjects\stroke_identification\myapp\healthcare_dataset_final_balanced_cleaned.csv"
df = pd.read_csv(file_path)

# Drop rows with missing values
df = df.dropna()

# Encode categorical features
categorical_cols = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Show encoding mapping
print("\n=== Label Encoding Mapping ===")
for col in encoders:
    print(f"{col} encoding: {dict(zip(encoders[col].classes_, encoders[col].transform(encoders[col].classes_)))}")

# Define features and target
X = df.drop(['stroke', 'id'], axis=1)
Y = df['stroke']

# Get categorical feature indices
categorical_feature_indices = [X.columns.get_loc(col) for col in categorical_cols]

# Apply SMOTENC for class imbalance
smote_nc = SMOTENC(categorical_features=categorical_feature_indices, random_state=42)
X_resampled, Y_resampled = smote_nc.fit_resample(X, Y)

# Format data
X_resampled_df = pd.DataFrame(X_resampled, columns=X.columns)
X_resampled_df["age"] = X_resampled_df["age"].round(0).astype(int)
X_resampled_df["avg_glucose_level"] = X_resampled_df["avg_glucose_level"].round(1)
X_resampled_df["bmi"] = X_resampled_df["bmi"].round(1)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_resampled_df, Y_resampled, test_size=0.2, random_state=42)

# Train model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Evaluate model
y_pred = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Show stroke-positive predictions
print("\n=== Sample Stroke Predictions ===")
for i in range(len(y_pred)):
    if y_pred[i] == 1:
        print("*****************")
        print(X_test.iloc[i].tolist())


# Function: Predict stroke class
def predict_rf_fn(row):
    return rf_model.predict([row])[0]


# Function: Feature-based severity classification
def classify_severity_based_on_features(row):
    age = row[1]
    glucose = row[7]
    bmi = row[8]

    if age >= 65 and glucose >= 140 and bmi >= 30:
        return "High"
    elif age >= 55 and (glucose >= 120 or bmi >= 28):
        return "Moderate"
    else:
        return "Mild"


# Function: Predict stroke and severity (based only on features)
def predict_stroke_and_severity(row):
    prediction = rf_model.predict([row])[0]

    if prediction == 0:
        return "Normal", "None"

    # Only use feature-based severity
    feature_severity = classify_severity_based_on_features(row)
    return "Stroke", feature_severity


# === Sample prediction test ===
sample_input = [1, 67, 0, 1, 1, 2, 0, 145, 32.5, 1]  # Example row
result, severity = predict_stroke_and_severity(sample_input)
print(f"\nSample Prediction: {result}, Severity: {severity}")
