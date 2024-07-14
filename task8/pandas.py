import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)
ages = df['Age']
print("Ages:\n", ages)
# Calculate the mean age
mean_age = df['Age'].mean()
print("Mean age:", mean_age)
