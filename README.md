
# README: Premier League Fantasy Player Ranking Script

## Overview

This Python script is designed to rank Premier League players based on their **Fantasy Premier League (FPL) score-to-cost ratio**. The ratio helps to identify players who provide the most value for their cost, making it easier to make informed decisions in the Fantasy Premier League.

## Features

- **Calculate Value**: Computes the ratio of each player's FPL score to their cost.
- **Rank Players**: Sorts players based on the score-to-cost ratio.
- **Export Ranked List**: Outputs the ranked list to a CSV file.

## Prerequisites

You need the following to run this script:
- **Python 3.x**
- **Pandas**: A Python library for data manipulation. You can install it by running:

```bash
pip install pandas
```

## Input Data Structure

The script expects a CSV file with the following columns:
- `Player Name` (Optional): Name of the player.
- `total_points`: Total FPL points accumulated by the player.
- `now_cost`: The current price of the player in the Fantasy Premier League.

### Example Input:

| Player Name   | total_points | now_cost |
|---------------|--------------|----------|
| Mohamed Salah | 210          | 12.5     |
| Harry Kane    | 180          | 12.0     |
| Kevin De Bruyne| 160         | 11.8     |

## How to Run

1. **Prepare the CSV File**:
   Ensure that you have a CSV file (`fpl_player_stats.csv`) containing the necessary player data (as shown in the Input Data Structure).

2. **Run the Script**:

   To execute the script, run the following command in your terminal:

   ```bash
   python rank_players.py
   ```

   Ensure the `fpl_player_stats.csv` file is in the same directory as the script, or adjust the `file_path` in the script to point to the correct file location.

3. **View the Output**:
   The script will create a new CSV file called `ranked_fpl_players.csv` in the same directory. This file contains the players ranked by their score-to-cost ratio.

## Output File

The output file (`ranked_fpl_players.csv`) will contain the following columns:
- `Player Name`: The name of the player.
- `total_points`: The player's total FPL points.
- `now_cost`: The player's current cost.
- `points_per_cost`: The ratio of total points to cost.
- `rank`: The rank of the player based on the score-to-cost ratio.

### Example Output:

| Player Name   | total_points | now_cost | points_per_cost | rank |
|---------------|--------------|----------|-----------------|------|
| Mohamed Salah | 210          | 12.5     | 16.8            | 1    |
| Kevin De Bruyne| 160         | 11.8     | 13.56           | 2    |
| Harry Kane    | 180          | 12.0     | 15.0            | 3    |

## Customization

You can easily modify the script to:
- Filter players by position or team.
- Adjust the output file name or location.
- Add more detailed analysis by extending the metrics calculated in the script.

## Troubleshooting

- **File Not Found Error**: Ensure that the file path for the input CSV is correct. If the file is not in the same directory as the script, update the `file_path` in the script to the full location of your CSV file.
- **Pandas Import Error**: If you encounter issues with `pandas`, ensure it is installed correctly by running `pip install pandas`.

## License

This project is licensed under the MIT License.

## Contact

If you have any questions or suggestions, feel free to reach out.
