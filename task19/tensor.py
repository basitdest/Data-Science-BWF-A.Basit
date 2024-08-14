import tensorflow as tf

# Creating a tensor
tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
print("Tensor:\n", tensor)

# Tensor operations
tensor_add = tf.add(tensor, 2)
tensor_mul = tf.multiply(tensor, 2)
print("Tensor after addition:\n", tensor_add)
print("Tensor after multiplication:\n", tensor_mul)
