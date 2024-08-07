import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# Create a scatter plot
sns.scatterplot(x='total_bill', y='tip', data=tips)

plt.title('Total Bill vs Tip')

plt.show()
