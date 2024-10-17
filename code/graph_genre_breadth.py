import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
df = pd.read_csv('artifacts/genre_audience_breadth.csv')

# Step 2: Set the first column as the new header then swap rows and columns
df.set_index(df.columns[0], inplace=True)
df_transposed = df.T

# Step 3: Format the data as percentages and round to the integer 
df_transposed = df_transposed.applymap(lambda x: f'{int(round(float(x) * 100))}%' if isinstance(x, (int, float)) else x)

# Step 4: Create the table
fig, ax = plt.subplots(figsize=(15, 10))  # Adjust the size of the figure for better spacing
ax.axis('tight')
ax.axis('off')

table = ax.table(cellText=df_transposed.values, colLabels=df_transposed.columns, rowLabels=df_transposed.index, 
                 cellLoc='center', loc='center')

# Step 5: do some adjustment to the head and row height
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 1.2)  # Increase the scale of the table

# Step 6: Set column headers (colLabels) to be vertical 
for (i, j), cell in table.get_celld().items():
    if i == 0:  # This is the header row
        cell.set_text_props(rotation=90, ha='center', va='bottom')  # Rotate to 90 degrees

# Step 7: Save the table as a PNG image
plt.title('Relationship between Genre and Audience Breadth by Content Rating Table', fontsize=16)
plt.savefig('artifacts/genre_audience_breadth_table_vertical.png', bbox_inches='tight')







