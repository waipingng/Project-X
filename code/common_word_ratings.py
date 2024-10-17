import os
import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Ensure the 'artifacts' folder exists (optional if it's already present)
os.makedirs('artifacts', exist_ok=True)

# Load the CSV file using a relative path
df = pd.read_csv('artifacts/movies.csv')

# Load stopwords from the stopwords file
with open('artifacts/stopwords.txt', 'r') as f:
    STOPWORDS = set(f.read().splitlines())

# Function to clean text and split into words
def clean_description(text):
    text = str(text).lower()  # Convert to lowercase
    text = re.sub(r'[^a-z\s]', '', text)  # Remove non-alphabetic characters
    words = text.split()  # Split text into words based on whitespace
    cleaned_words = [word for word in words if word not in STOPWORDS]  # Remove stopwords
    return cleaned_words

# Apply the cleaning function to each description
df['cleaned_description'] = df['description'].apply(clean_description)

# Flatten list of all words across descriptions
all_words = [word for desc in df['cleaned_description'] for word in desc]

# Calculate word frequency
word_counts = Counter(all_words)
most_common_words = word_counts.most_common(30)  # Top 30 most frequent words

# Create a DataFrame to store the most common words and their frequencies
df_word_freq = pd.DataFrame(most_common_words, columns=['Word', 'Frequency'])

# Save the word frequency data to CSV in the artifacts folder
csv_path = 'artifacts/word_frequencies.csv'
df_word_freq.to_csv(csv_path, index=False)
print(f"Word frequencies saved to {csv_path}")

# Analyze correlation between frequency of top words and movie ratings
for word, _ in most_common_words:
    df[word] = df['cleaned_description'].apply(lambda desc: desc.count(word))

# Compute correlation of word frequencies with ratings
correlations = {word: pearsonr(df[word], df['rating'])[0] for word in df_word_freq['Word']}

# Display correlations
print("Correlation between word frequencies and ratings:")
for word, corr in correlations.items():
    print(f"{word}: {corr:.2f}")

# Plot correlations
plt.figure(figsize=(10, 6))
plt.barh(list(correlations.keys()), list(correlations.values()))
plt.xlabel('Correlation with Rating')
plt.ylabel('Word')
plt.title('Correlation of Word Frequencies with Movie Ratings')

# Save the plot as an image in the artifacts folder
plot_path = 'artifacts/word_frequencies_plot.png'
plt.savefig(plot_path, bbox_inches='tight')
print(f"Plot saved to {plot_path}")

# If running interactively, show the plot
plt.show()
