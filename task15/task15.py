import numpy as np


# Reshaping arrays
array1 = np.array([1, 2, 3, 4, 5, 6])
reshaped_array = array1.reshape((2, 3))
print("Original Array:", array1)
print("Reshaped Array (2x3):\n", reshaped_array)

# Concatenation
array2 = np.array([[7, 8, 9], [10, 11, 12]])
concatenated_array = np.concatenate((reshaped_array, array2), axis=0)
print("\nArray to Concatenate:\n", array2)
print("Concatenated Array (along axis 0):\n", concatenated_array)

# Splitting arrays
split_array = np.split(array1, 3)
print("\nOriginal Array for Splitting:", array1)
print("Split Array into 3 parts:", split_array)

# Horizontal splitting (hsplit)
array3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
hsplit_array = np.hsplit(array3, 2)
print("\nOriginal Array for Hsplit:\n", array3)
print("Horizontally Split Array into 2 parts:\n", hsplit_array)
