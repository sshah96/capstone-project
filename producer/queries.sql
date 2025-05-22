CREATE OR REPLACE STREAM nba_reg_season_stats(
    TEAM_ABBREVIATION STRING,
    GP INTEGER,
    REB INTEGER,
    AST INTEGER,
    PTS INTEGER,
    PERSON_ID STRING
) WITH (
    KAFKA_TOPIC = 'reg-season-stats',
    VALUE_FORMAT = 'JSON'
);

CREATE OR REPLACE STREAM nba_live_playoff_stats(
    PERSONID STRING,
    NAME STRING,
    JERSEYNUM STRING,
    POSITION STRING,
    TEAMTRICODE STRING,
    PLAYERSLUG STRING,
    POINTS INTEGER,
    REBOUNDS INTEGER,
    ASSISTS INTEGER
) WITH (
    KAFKA_TOPIC = 'reg-season-stats',
    VALUE_FORMAT = 'JSON'
);

CREATE OR REPLACE STREAM playoff_reg_season_combined AS
SELECT
        p.PERSONID,
        p.NAME as name,
        p.position as position,
        r.team_abbreviation as team,
        p.points as playoff_pts,
        p.rebounds as playoff_reb,
        p.assists as playoff_ast,
        r.gp as games_played,
        r.reb as reb,
        r.ast as ast,
        r.pts as pts
    FROM  NBA_LIVE_PLAYOFF_STATS p
    INNER JOIN  NBA_REG_SEASON_STATS r
    WITHIN 2 DAYS
        ON p.PERSONID = r.PERSON_ID;


CREATE OR REPLACE STREAM playoff_reg_season_delta AS
SELECT
        p.PERSONID,
        p.NAME as name,
        p.position as position,
        p.team as team,
        p.playoff_pts - (pts / games_played) as pts_above_reg_season,
        p.playoff_reb - (reb / games_played) as reb_above_reg_season,
        p.playoff_ast - (ast / games_played) as ast_above_reg_season
    FROM PLAYOFF_REG_SEASON_COMBINED p;
