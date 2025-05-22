# capstone-project
Final Project for DE Bootcamp

Start by going to data_test.py and seeing what data for players you get. Notes:
1. The live data element is the current scoreboard (the games currently being played). If there are no games being played currently, it is showing the most recent set of games.
2. We only get the data associated with each team's scoring leader.
3. We then query the NBA API to get the player's current season statistics.
4. This file should generate newline delimited json for the live game (stat leaders) as well as their respective season statistics.