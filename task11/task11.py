import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

# Linear Regression aka Supervised Learning
def linear_regression_demo():
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([1, 3, 2, 3, 5])
    
    model = LinearRegression()
    model.fit(X, y)
    
    y_pred = model.predict(X)
    
    plt.scatter(X, y, color='blue', label='Original data')
    plt.plot(X, y_pred, color='red', label='Fitted line')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.title('Linear Regression')
    plt.show()

# K Means aka Unsupervised Learning
def kmeans_clustering_demo():
    X = np.array([[1, 2], [2, 3], [3, 4], [5, 7], [6, 8], [7, 9]])
    
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(X)
    
    y_kmeans = kmeans.predict(X)
    
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('K-Means Clustering')
    plt.show()

# Q Learning aka Reinforcement learning
def q_learning_demo():
    import numpy as np
    
    # Define the environment
    states = ["A", "B", "C", "D"]
    actions = ["left", "right"]
    Q = np.zeros((len(states), len(actions)))

    # Define rewards and transitions
    rewards = {"A": {"left": 0, "right": 1},
               "B": {"left": 0, "right": 1},
               "C": {"left": 0, "right": 1},
               "D": {"left": 0, "right": 1}}

    transitions = {"A": {"left": "A", "right": "B"},
                   "B": {"left": "A", "right": "C"},
                   "C": {"left": "B", "right": "D"},
                   "D": {"left": "C", "right": "D"}}

    # Q-Learning parameters
    alpha = 0.1
    gamma = 0.9
    epsilon = 0.1

    # Training
    for episode in range(1000):
        state = "A"
        while state != "D":
            if np.random.rand() < epsilon:
                action = np.random.choice(actions)
            else:
                action = actions[np.argmax(Q[states.index(state)])]
            
            next_state = transitions[state][action]
            reward = rewards[state][action]
            Q[states.index(state), actions.index(action)] += alpha * (
                reward + gamma * np.max(Q[states.index(next_state)]) - Q[states.index(state), actions.index(action)]
            )
            state = next_state

    print("Trained Q-Table:")
    print(Q)

# Main function to run all demos
def main():
    print("Supervised Learning: Linear Regression")
    linear_regression_demo()
    
    print("Unsupervised Learning: K-Means Clustering")
    kmeans_clustering_demo()
    
    print("Reinforcement Learning: Q-Learning")
    q_learning_demo()

if __name__ == "__main__":
    main()
