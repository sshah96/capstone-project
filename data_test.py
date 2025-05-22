from nba_api.live.nba.endpoints import scoreboard
from nba_api.live.nba.endpoints import boxscore
from nba_api.stats.endpoints import playerdashboardbyyearoveryear

games = scoreboard.ScoreBoard()
box_score = boxscore.BoxScore('0042400301')

score = games.get_json()

box_score_dict = box_score.get_dict()
# print(box_score_dict['game']['homeTeam']['players'][0])

career = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear('1628384')
# print(career.get_data_frames()[0]['REB'] / career.get_data_frames()[0]['GP'] )

print(score)