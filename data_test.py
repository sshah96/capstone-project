from nba_api.live.nba.endpoints import scoreboard
from nba_api.live.nba.endpoints import boxscore
from nba_api.stats.endpoints import playerdashboardbyyearoveryear
import json

games = scoreboard.ScoreBoard()
box_score = boxscore.BoxScore('0042400301')

score = games.get_dict()

with open("nba_score.json", "w") as f:
    json.dump(score, f)

f.close()



box_score_dict = box_score.get_dict()
# print(box_score_dict['game']['homeTeam']['players'][0])

career = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear('1628384')
# print(career.get_data_frames()[0]['REB'] / career.get_data_frames()[0]['GP'] )
games = score['scoreboard']['games']
for game in games:
    player_id_home = game['gameLeaders']['homeLeaders']['personId']
    player_id_away = game['gameLeaders']['awayLeaders']['personId']
    career_home = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(f'{player_id_home}')
    career_away = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(f'{player_id_away}')
    with open("home_player_stats.json", "w") as f1:
        json.dump(career_home.get_dict(), f1)
    f1.close()
    with open("away_player_stats.json", "w") as f2:
        json.dump(career_away.get_dict(), f2)
    f2.close()

# print(score['scoreboard']['games'][0]['gameLeaders']['homeLeaders'])
# print(len(score['scoreboard']['games']))