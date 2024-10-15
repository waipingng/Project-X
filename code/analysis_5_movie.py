def main():
    movies_df = scrape_imdb_top_250()
def calculate_avg_box_office_by_gender(movies_df):
    # Grouping by 'Lead Actor Gender' and calculating the average box office revenue
    avg_box_office_by_gender = movies_df.groupby('Lead Actor Gender')['Box Office'].mean().sort_values(ascending=False)

    print("Average Box Office Revenue by Lead Actor Gender:")
    print(avg_box_office_by_gender)
    return avg_box_office_by_gender

# Running the function to calculate the average box office revenue by gender
avg_box_office_by_gender = calculate_avg_box_office_by_gender(movies_df)


def calculate_avg_box_office_by_ethnicity(movies_df):
    # Grouping by 'Lead Actor Ethnicity' and calculating the average box office revenue
    avg_box_office_by_ethnicity = movies_df.groupby('Lead Actor Ethnicity')['Box Office'].mean().sort_values(ascending=False)

    print("Average Box Office Revenue by Lead Actor Ethnicity:")
    print(avg_box_office_by_ethnicity)
    return avg_box_office_by_ethnicity

# Run the function to calculate the average box office revenue by ethnicity
avg_box_office_by_ethnicity = calculate_avg_box_office_by_ethnicity(movies_df)

if __name__ == "__main__":
    main()#diversity in lead actors and film success#diversity in lead actors and film success