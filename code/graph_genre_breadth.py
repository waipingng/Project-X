
import pandas as pd
import matplotlib.pyplot as plt
import math

# Step 1: read the file
df = pd.read_csv('artifacts/genre_audience_breadth.csv')

# Step 2: Set the first column as the new header then swap rows and columns
df.set_index(df.columns[0], inplace=True)
df_transposed = df.T

# Step 3: Format the data as percentages, round to the nearest integer 
df_transposed = df_transposed.astype(float).map(lambda x: x * 100).round(0).astype(int).astype(str) + '%'

# Step 4: Split the table into two parts (half columns each)
mid_index = math.ceil(len(df_transposed.columns) / 2)
df_split1 = df_transposed.iloc[:, :mid_index]  
df_split2 = df_transposed.iloc[:, mid_index:]  

# Step 5: Create the figure for the first half
fig1, ax1 = plt.subplots(figsize=(10, 7))  
ax1.axis('tight')
ax1.axis('off')

table1 = ax1.table(cellText=df_split1.values, colLabels=df_split1.columns, rowLabels=df_split1.index, 
                   cellLoc='center', loc='center')

# Step 6: Adjust font size and scale for first table, reduce the header row height
table1.auto_set_font_size(False)
table1.set_fontsize(12)
table1.scale(2.0, 2.0) 
for (i, j), cell in table1.get_celld().items():
    if i == 0:  
        cell.set_text_props(rotation=90, ha='center', va='bottom')
        cell.set_height(0.15)  

# Step 7: Save the first part 
plt.title('Relationship between Genre and Audience Breadth by Content Rating (Part 1)', fontsize=14, pad=20)
plt.savefig('artifacts/genre_audience_breadth_table_part1.png', bbox_inches='tight')

# Step 8: Create the figure for the second half
fig2, ax2 = plt.subplots(figsize=(10, 7))  
ax2.axis('tight')
ax2.axis('off')

table2 = ax2.table(cellText=df_split2.values, colLabels=df_split2.columns, rowLabels=df_split2.index, 
                   cellLoc='center', loc='center')

# Step 9: Adjust font size and scale for second table, widen the cells
table2.auto_set_font_size(False)
table2.set_fontsize(12)
table2.scale(2.5, 2.5)  
for (i, j), cell in table2.get_celld().items():
    if i == 0:  
        cell.set_text_props(rotation=90, ha='center', va='bottom')
        cell.set_height(0.15)  

# Step 10: Add footnote indicating values are percentages
plt.figtext(0.5, 0.01, 'My values in the graph are rounded to the nearest whole percentage', ha='center', fontsize=12)

# Step 11: Save the second part
plt.title('Relationship between Genre and Audience Breadth by Content Rating (Part 2)', fontsize=14, pad=20)
plt.savefig('artifacts/genre_audience_breadth_table_part2.png', bbox_inches='tight')