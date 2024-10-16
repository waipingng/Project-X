import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file generated from your previous script
length_count = pd.read_csv('artifacts/movie_length.csv')

# Step 2: Plot the bar graph
plt.figure(figsize=(8, 6))
plt.bar(length_count['movie length'], length_count['frequency'], color=['blue', 'green', 'red'])

# Step 3: Customize the plot
plt.title('Frequency of Movie Length Categories', fontsize=14)
plt.xlabel('Movie Length Category', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Step 4: Save the plot as an image file
plt.tight_layout()
plt.savefig('artifacts/movie_length_plot.png')

# Step 5: Show the plot
plt.show()
