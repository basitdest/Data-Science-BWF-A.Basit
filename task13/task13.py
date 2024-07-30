import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Sample dataset to demonstrate drop_duplicates and missing values
data = {
    'A': [1, 2, np.nan, 4, 5, 6, 7, 8, 9, 10],
    'B': [5, np.nan, 6, 8, 8, np.nan, 9, 10, 10, 11],
    'C': ['a', 'b', 'b', 'c', 'd', 'd', 'd', 'e', 'e', 'e'],
    'D': [1, 2, 2, 3, 4, 4, 4, 5, 5, 6]
}
df = pd.DataFrame(data)


print("Original DataFrame:")
print(df)

# Fill missing values with the mean of the column
df['A'].fillna(df['A'].mean(), inplace=True)
df['B'].fillna(df['B'].mean(), inplace=True)
print("\nDataFrame after filling missing values:")
print(df)

df = df.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(df)

# Removing Outliers using IQR method
Q1 = df['A'].quantile(0.25)
Q3 = df['A'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df = df[(df['A'] >= lower_bound) & (df['A'] <= upper_bound)]
print("\nDataFrame after removing outliers:")
print(df)

# 4. Decision Tree Classification
# X= features and Y= target
X = df[['A', 'B']]
y = df['D']

# Split the dataset 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"\nDecision Tree Classifier Accuracy: {accuracy:.2f}")

# Visualize the Decision Tree
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=['A', 'B'], class_names=[str(i) for i in df['D'].unique()], filled=True)
plt.title('Decision Tree')
plt.show()
