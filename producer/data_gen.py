from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import playerdashboardbyyearoveryear
import json
import ndjson
import pandas as pd

games = scoreboard.ScoreBoard()

score = games.get_dict()

relevant_data = []

games = score['scoreboard']['games']

print(games)
for game in games:

    player_home_stats = game['gameLeaders']['homeLeaders']
    player_away_stats = game['gameLeaders']['awayLeaders']
    with open("nba_score.ndjson", "w") as f:
        ndjson.dump([player_home_stats, player_away_stats], f)
    player_id_home = player_home_stats['personId']
    player_id_away = player_away_stats['personId']
    career_home = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(f'{player_id_home}').get_data_frames()[0]
    career_home = career_home.iloc[:, 2:30]
    career_home['PERSON_ID'] = player_id_home
    career_away = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(f'{player_id_away}').get_data_frames()[0]
    career_away = career_away.iloc[:, 2:30]
    career_away['PERSON_ID'] = player_id_away

    all_player_stats = pd.concat([career_home, career_away])

    all_player_stats.to_json("player_stats.ndjson",
            orient="records",
            lines=True)
    
# Future work: get more data than just the leaders!
# box_score_dict = box_score.get_dict()
# print(box_score_dict['game']['homeTeam']['players'])
# box_score = boxscore.BoxScore('0042400301')