import pandas as pd  

# Step 1: Read the CSV file into a DataFrame
def read_csv_to_dataframe(csv_file):
    return pd.read_csv(csv_file)

# Step 2: Classify ratings into categories for each score
def classify_rating(rating):
    return round(rating, 2)  # Round the rating to 2 decimal places

# Step 3: Count ratings by category and content rating
def count_ratings(df):
    df['rating_category'] = df['rating'].apply(classify_rating)
    
    # Count occurrences for each content rating under each rating category
    count_df = df.groupby(['rating_category', 'content_rating']).size().unstack(fill_value=0)
    
    # Calculate total occurrences for each content rating
    total_counts = df['content_rating'].value_counts()
    
    # Calculate frequency as a proportion of total counts
    frequency_df = count_df.div(total_counts, axis=1).fillna(0)
    
    # Round the frequency to 2 decimal places
    frequency_df = frequency_df.round(2)
    
    # Reset the index for saving
    frequency_df.columns.name = None  
    frequency_df.reset_index(inplace=True)
    
    return count_df, total_counts, frequency_df

# Step 4: Save the result to a CSV file
def save_to_csv(df, output_file):
    df.to_csv(output_file, index=False)

# Main execution
if __name__ == "__main__":
    input_file = 'artifacts/movies.csv'
    output_file = 'artifacts/rating_frequency.csv'  # Updated output file name

    df = read_csv_to_dataframe(input_file)
    count_df, total_counts, frequency_df = count_ratings(df)
    
    # Save count_df and frequency_df to separate files if needed
    save_to_csv(count_df, 'artifacts/rating_count.csv')  # Optionally save counts
    save_to_csv(frequency_df, output_file)  # Save frequency to the specified file
