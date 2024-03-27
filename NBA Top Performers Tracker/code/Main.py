import requests
import pandas as pd
import csv
import Player
import datetime
import os


def createPlayers(filepath):
    # init a list to store player objects
    players = []

    # opens the csv file for reading
    with open(filepath, 'r') as csv_f:
        csv_reader = csv.reader(csv_f)

        # skips header row
        next(csv_f)

        # gets player data and uses it to create a player object
        for line in csv_reader:
            name = line[1]
            team_id = line[3]
            team = line[4]
            minutes = line[10]
            fgm = line[11]
            fga = line[12]
            fg3m = line[14]
            fg3a = line[15]
            ftm = line[17]
            fta = line[18]
            dreb = line[21]
            oreb = line[20]
            ast = line[23]
            tov = line[24]
            stl = line[25]
            blk = line[26]
            pfoul = line[28]
            pts = line[30]
            stats = [pts, dreb, oreb, ast, stl, blk, tov, fgm, fga, fg3m, fg3a, ftm, fta, pfoul]

            player = Player.Player(name, team, team_id, minutes, stats)
            players.append(player)

    # returns a list of player objects
    return players

def scrapeStats(date, filepath):

        year = date[0:4]
        month = date[5:7]
        day = date[8:10]

        # url info
        #season_id = "2023-24"
        #per_mode = "Totals"

        # nba stats table endpoint url
        url_start = "https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom={}%2F{}%2F{}&DateTo={}%2F{}%2F{}&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&ISTRound=&LastNGames=1&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2023-24&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="
        url = url_start.format(month, day, year, month, day, year)

        # headers for bot detection bypass
        headers  = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'x-nba-stats-token': 'true',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'x-nba-stats-origin': 'stats',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Referer': 'https://stats.nba.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        # gets request from url and stores response
        response = requests.get(url=url, headers=headers).json()
        # stores player info from the stats table
        player_info = response['resultSets'][0]['rowSet']

        # column headers for data frame 
        columns_list = [ 
            "PLAYER_ID",
            "PLAYER_NAME",
            "NICKNAME",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "AGE",
            "GP",
            "W",
            "L",
            "W_PCT",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT", 
            "OREB", 
            "DREB", 
            "REB", 
            "AST", 
            "TOV", 
            "STL", 
            "BLK", 
            "BLKA", 
            "PF", 
            "PFD", 
            "PTS", 
            "PLUS_MINUS", 
            "NBA_FANTASY_PTS", 
            "DD2",
            "TD3",
            "WNBA_FANTASY_PTS",
            "GP_RANK", 
            "W_RANK",
            "L_RANK",
            "W_PCT_RANK", 
            "MIN_RANK", 
            "FGM_RANK", 
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "FTM_RANK",
            "FTA_RANK",
            "FT_PCT_RANK",
            "OREB_RANK",
            "DREB_RANK",
            "REB_RANK",
            "AST_RANK",
            "TOV_RANK",
            "STL_RANK",
            "BLK_RANK",
            "BLKA_RANK",
            "PF_RANK",
            "PFD_RANK",
            "PTS_RANK",
            "PLUS_MINUS_RANK",
            "NBA_FANTASY_PTS_RANK",
            "DD2_RANK",
            "TD3_RANK",
            "WNBA_FANTASY_PTS_RANK"
        ]

        # creates data frame for the stats table
        nba_df = pd.DataFrame(player_info, columns = columns_list)
        # stores the data frame as a csv file in the given filepath 
        nba_df.to_csv(filepath, index=False)


if __name__ == "__main__":
 
    # gets yesterdays date in order to display stats for yesterdays games
    yesterday = (datetime.datetime.now() - datetime.timedelta(days = 1)).strftime("20%y-%m-%d")

    # creates the filepath string for the stats csv file
    filepath = os.getcwd() + '\stats\{}-stats.csv'.format(yesterday)

    scrapeStats(yesterday, filepath)
    players = createPlayers(filepath)

    top_players = sorted(players, key=lambda player: player.pts, reverse=True)
    
    for i in range(10):
        print(str(top_players[i]))
   
    



