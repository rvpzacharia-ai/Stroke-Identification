import csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_squared_error, r2_score

# Prepare data lists
X_classification = []
Y_classification = []

X_regression = []
Y_regression = []

# Load data
# Load data
file_path = r"C:\Users\kshiv\PycharmProjects\stroke_identification\myapp\stroke_risk_dataset.csv"
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        try:
            row = [cell.strip() for cell in row]  # Remove extra spaces
            features = list(map(float, row[:-2]))  # 16 features: 15 symptoms + Age
            stroke_risk_percent = float(row[-2])   # For regression
            at_risk_binary = int(row[-1])          # For classification

            # Store data
            X_classification.append(features)
            Y_classification.append(at_risk_binary)

            X_regression.append(features)
            Y_regression.append(stroke_risk_percent)

        except Exception as e:
            print("Skipping row due to error:", row)
            print("Error:", e)
            continue


# Check if we loaded data
if len(X_classification) == 0:
    print("No valid data found. Please check your CSV format.")
    exit()

print("Total Samples:", len(X_classification))
print("First sample:", X_classification[0])
print("First label:", Y_classification[0])

# ======== Classification ========
# Train/Test Split
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_classification, Y_classification, test_size=0.2, random_state=42)

# Scale features
scaler_c = StandardScaler()
X_train_c_scaled = scaler_c.fit_transform(X_train_c)
X_test_c_scaled = scaler_c.transform(X_test_c)

# Create and train KNN Classifier
knn_classifier = KNeighborsClassifier(n_neighbors=5)
knn_classifier.fit(X_train_c_scaled, y_train_c)

# Predict and evaluate
y_pred_c = knn_classifier.predict(X_test_c_scaled)

print("\n--- KNN Classification ---")
print("Accuracy:", accuracy_score(y_test_c, y_pred_c))
print("Confusion Matrix:\n", confusion_matrix(y_test_c, y_pred_c))
print("Classification Report:\n", classification_report(y_test_c, y_pred_c))


# ======== Optional: Regression for Stroke Risk (%) ========
do_regression = True  # Set to False if you only want classification

if do_regression:
    X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_regression, Y_regression, test_size=0.2, random_state=42)

    scaler_r = StandardScaler()
    X_train_r_scaled = scaler_r.fit_transform(X_train_r)
    X_test_r_scaled = scaler_r.transform(X_test_r)

    knn_regressor = KNeighborsRegressor(n_neighbors=5)
    knn_regressor.fit(X_train_r_scaled, y_train_r)

    y_pred_r = knn_regressor.predict(X_test_r_scaled)

    print("\n--- KNN Regression (Stroke Risk %) ---")
    print("MSE:", mean_squared_error(y_test_r, y_pred_r))
    print("R² Score:", r2_score(y_test_r, y_pred_r))
def predict_user_input(user_input_features):
    """
    user_input_features: list of 16 values (15 symptoms + age)
    Returns:
      - risk_percent: float
      - risk_binary: int (0 or 1)
    """
    # Scale input for regression
    input_scaled_r = scaler_r.transform([user_input_features])
    risk_percent = knn_regressor.predict(input_scaled_r)[0]

    # Scale input for classification
    input_scaled_c = scaler_c.transform([user_input_features])
    risk_binary = knn_classifier.predict(input_scaled_c)[0]

    return round(risk_percent, 2), int(risk_binary)

# import csv
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# from imblearn.over_sampling import SMOTE
# import numpy as np
#
# # Prepare data lists
# X = []
# Y = []
#
# # Load data
# file_path = "stroke_risk_dataset.csv"
# with open(file_path, mode='r') as file:
#     csv_reader = csv.reader(file)
#     header = next(csv_reader)  # Skip header
#
#     for row in csv_reader:
#         try:
#             features = list(map(float, row[:-1]))  # All columns except last = features
#             target = int(row[-1])  # Last column = At Risk (0 or 1)
#             X.append(features)
#             Y.append(target)
#         except:
#             continue  # skip any invalid row
#
# print("Original Samples:", len(X))
#
# if len(X) == 0:
#     print("❌ No valid data found. Please check your CSV file.")
#     exit()
#
# # Convert to numpy arrays
# X = np.array(X)
# Y = np.array(Y)
#
# # Apply SMOTE (for continuous/numerical features)
# sm = SMOTE(random_state=42)
# X_resampled, Y_resampled = sm.fit_resample(X, Y)
#
# print("After SMOTE → Total Samples:", len(X_resampled))
#
# # Train/Test Split
# X_train, X_test, y_train, y_test = train_test_split(X_resampled, Y_resampled, test_size=0.2, random_state=42)
#
# # Scale features
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)
#
# # Create and train KNN
# knn_model = KNeighborsClassifier(n_neighbors=5)
# knn_model.fit(X_train_scaled, y_train)
#
# # Predict and evaluate
# y_pred = knn_model.predict(X_test_scaled)
#
# print("\n✅ Accuracy:", accuracy_score(y_test, y_pred))
# print("\n📊 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
# print("\n📄 Classification Report:\n", classification_report(y_test, y_pred))
