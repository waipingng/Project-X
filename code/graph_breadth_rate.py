import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
df = pd.read_csv('artifacts/rating_frequency.csv')

# Step 2: Set the style for the plots
plt.style.use('ggplot') 

# Step 3: Create a function to plot the data
def plot_data(x, y, label, title, color, marker):
    plt.plot(x, y, marker=marker, label=label, color=color)
    plt.fill_between(x, y, color=color, alpha=0.1)

# Define x (rating categories)
x_labels = df['rating_category'].values

# Plot 1: R and G on the same graph
plt.figure(figsize=(12, 6))
y_r = df['R'].values
plot_data(x_labels, y_r, 'R', 'Frequency of R and G Ratings', 'red', 'o')

y_g = df['G'].values
plot_data(x_labels, y_g, 'G', 'Frequency of G Ratings', 'orange', 'D')

for i, (r, g) in enumerate(zip(y_r, y_g)):
    plt.text(i, r + 0.02, 'PG-13', color='red', fontsize=12, ha='center')
    plt.text(i, g + 0.02, 'G', color='orange', fontsize=12, ha='center')

# Customize the plot
plt.figtext(0.1, 0.01, 'frequency=count/total', ha='center', fontsize=12)
plt.title('Frequency of R and G Content Ratings by Rating Category')
plt.xlabel('Rating Category')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  
plt.legend()

# Save the plot with new name
plt.savefig('artifacts/R-G-rate.png')


# Plot 2: PG-13 and G on the same graph
plt.figure(figsize=(12, 6))
y_pg13 = df['PG-13'].values
plot_data(x_labels, y_pg13, 'PG-13', 'Frequency of PG-13 and G Ratings', 'green', '^')

# Re-plot G on the same graph
plot_data(x_labels, y_g, 'G', 'Frequency of G Ratings', 'orange', 'D')

# Adding annotations for PG-13 and G
for i, (pg13, g) in enumerate(zip(y_pg13, y_g)):
    plt.text(i, pg13 + 0.02, 'PG-13', color='green', fontsize=12, ha='center')
    plt.text(i, g + 0.02, 'G', color='orange', fontsize=12, ha='center')

# Customize the third plot
plt.figtext(0.1, 0.01, 'frequency=count/total', ha='center', fontsize=12)
plt.title('Frequency of PG-13 and G Content Ratings by Rating Category')
plt.xlabel('Rating Category')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Draw a horizontal line at y=0
plt.legend()


# Save the third plot with new name
plt.savefig('artifacts/PG-13-G-rate.png')
 

plt.show()