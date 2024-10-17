import pandas as pd
csv_file = 'artifacts/movies.csv'
# Step 1: Read the CSV file into a DataFrame
def read_csv_to_dataframe(csv_file):
    return pd.read_csv(csv_file)

# Step 2: Classify ratings into categories
def classify_rating(rating):
    if 8.0 <= rating <= 8.2:
        return '8.0-8.2'
    if 8.3 <=rating <= 8.4:
        return '8.2-8.4'
    elif rating == 8.5:
        return '8.5'
    elif 8.6 <= rating <= 8.7:
        return '8.6-8.7'
    elif 8.8 <= rating <= 8.9:
        return '8.8-8.9'
    elif 9.0 <= rating <= 9.3:
        return '9-9.3'
    else:
        return 'Other'

# Step 3: Count ratings by category and content rating
def count_ratings(df):
    df['rating_category'] = df['rating'].apply(classify_rating)
    count_df = df.groupby(['rating_category', 'content_rating']).size().unstack(fill_value=0)
    count_df.columns.name = None  
    count_df.reset_index(inplace=True)
    return count_df

# Step 4: Save the result to a  CSV file
def save_to_csv(df, output_file):
    """Saves the DataFrame to a CSV file."""
    df.to_csv(output_file, index=False)

# Main execution
if __name__ == "__main__":
    input_file = 'artifacts/movies.csv'
    output_file = 'artifacts/breadth_rate.csv'

    df = read_csv_to_dataframe(input_file)
    count_df = count_ratings(df)
    save_to_csv(count_df, output_file)
