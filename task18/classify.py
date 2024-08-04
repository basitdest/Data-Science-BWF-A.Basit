import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import sqlite3

# Load the dataset
data = pd.read_csv('Iris.csv')

# Print the first few rows and column names to inspect the data
print("First few rows of the dataset:")
print(data.head())
print("\nColumn names:")
print(data.columns)

# Check if 'species' column exists
if 'Species' not in data.columns:
    raise KeyError("The 'species' column is not found in the dataset.")

# Preprocess the data
X = data.drop('Species', axis=1)  # Features
y = data['Species']  # Target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train a classification model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print('Classification Report:')
print(report)
print('Confusion Matrix:')
print(conf_matrix)

# Store results in SQLite database
conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()

# Create a table to store the results
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ModelResults (
        id INTEGER PRIMARY KEY,
        accuracy REAL,
        report TEXT
    )
''')

# Insert the results into the table
cursor.execute('''
    INSERT INTO ModelResults (accuracy, report)
    VALUES (?, ?)
''', (accuracy, report))

# Commit the transaction and close the connection
conn.commit()
conn.close()

# Visualizations
# Pairplot of the dataset
sns.pairplot(data, hue='Species')
plt.title('Pairplot of the Iris Dataset')
plt.show()

# Heatmap of the confusion matrix
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=data['species'].unique(), yticklabels=data['species'].unique())
plt.title('Confusion Matrix Heatmap')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Distribution plot of each feature
for column in X.columns:
    plt.figure()
    sns.histplot(data[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.show()
