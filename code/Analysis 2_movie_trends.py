import matplotlib.pyplot as plt

def plot_rating_trends_over_time(movies_df):
    # Group by year and calculate the average rating for each year
    avg_rating_by_year = movies_df.groupby('Year')['Rating'].mean()

    # Plot the average rating by year
    plt.plot(avg_rating_by_year.index, avg_rating_by_year.values)
    plt.xlabel('Year')
    plt.ylabel('Average IMDb Rating')
    plt.title('Average IMDb Rating Over Time')
    plt.show()

# Run the function to plot IMDb ratings over time
plot_rating_trends_over_time(movies_df)