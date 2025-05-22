# capstone-project
Final Project for DE Bootcamp

Start by going to data_gen.py and seeing what data for players you get. Notes:
1. The live data element is the current scoreboard (the games currently being played). If there are no games being played currently, it is showing the most recent set of games.
2. We only get the data associated with each team's scoring leader.
3. We then query the NBA API to get the player's current season statistics.
4. This file should generate newline delimited json for the live game (stat leaders) as well as their respective season statistics.

Then you run producer.py on the command line with the appropriate arguments (config file with the correct user and password and the topic you want to publish to). You also want to modify the ndjson file that producer.py reads in (e.g. player_stats is for the regular season and nba_score is for the playoffs - I have published these datasets to separate topics to correspond to that).

Once you have published the messages to the topics your Confluent page should look like this:

![images/topics.png](images/topics.png)
