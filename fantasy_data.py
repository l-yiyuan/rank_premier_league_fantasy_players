import requests
import pandas as pd

# URL for the unofficial FPL API that provides player stats
url = "https://fantasy.premierleague.com/api/bootstrap-static/"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Extract player data
    players = data['elements']
    player_df = pd.DataFrame(players)

    # Extract team data
    teams = data['teams']
    team_df = pd.DataFrame(teams)

    # Extract position data
    positions = data['element_types']
    position_df = pd.DataFrame(positions)

    # Map team and position IDs to names
    player_df['team_name'] = player_df['team'].map(team_df.set_index('id')['name'])
    player_df['position'] = player_df['element_type'].map(position_df.set_index('id')['singular_name'])

    # Select relevant columns for display
    selected_columns = ['first_name', 'second_name', 'team_name', 'position', 'total_points', 'goals_scored', 'assists', 'minutes', 'now_cost']
    readable_df = player_df[selected_columns]

    # Display the first few rows of the readable DataFrame
    print(readable_df.head())

    # Save the data to a CSV file
    readable_df.to_csv('fpl_player_stats.csv', index=False)
    print("Data saved to 'fpl_player_stats.csv'")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")



