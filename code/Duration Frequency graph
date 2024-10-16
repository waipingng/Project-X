import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the CSV file generated from your previous script
length_count = pd.read_csv('artifacts/movie_length.csv')

# Step 2: Plot the bar graph using seaborn
plt.figure(figsize=(8, 6))
sns.barplot(x='movie length', y='frequency', data=length_count, palette='coolwarm')

# Step 3: Customize the plot
plt.title('Frequency of Movie Length Categories', fontsize=14)
plt.xlabel('Movie Length Category', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Step 4: Show the plot
plt.tight_layout()
plt.show()
