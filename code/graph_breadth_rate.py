import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file into a DataFrame
input_file = 'artifacts/breadth_rate.csv'  # Your CSV file path
df = pd.read_csv(input_file)

# Step 2: Set the rating_category as index 
df.set_index('rating_category', inplace=True)

# Step 3: Plotting the bar chart
ax = df.plot(kind='bar', figsize=(12, 6), width=0.8)

# Step 4: Set the title and labels
plt.title('The Relationship Between Rate and Audience Breadth', fontsize=16)
plt.xlabel('Rating Category', fontsize=14)
plt.ylabel('Count', fontsize=14)

# Step 5: Show the legend
plt.legend(title='Content Rating')

# Step 6: Show the plot
plt.tight_layout() 

# Step 7: Save as a PNG image
plt.savefig('artifacts/rate_audience_breadth.png', bbox_inches='tight')
