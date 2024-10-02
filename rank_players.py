import pandas as pd

# Load the CSV file
file_path = 'fpl_player_stats.csv' 
df = pd.read_csv('fpl_player_stats.csv')

# Calculate the ranking metric (total_points/now_cost)
df['points_per_cost'] = df['total_points'] / df['now_cost']

# Rank the players based on the calculated metric
df['rank'] = df['points_per_cost'].rank(ascending=False)

# Sort the DataFrame by rank
ranked_df = df.sort_values(by='rank')

# Write the entire ranked DataFrame to a new CSV file
output_file_path = 'ranked_fpl_players.csv' 
ranked_df.to_csv('ranked_fpl_players.csv', index=False)

print(f"The entire ranked list of players has been saved to {'ranked_fpl_players.csv'}")
