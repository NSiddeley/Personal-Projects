class Player:
    def __init__(self, name, team, team_id, minutes, stats):
        self.name = name
        self.team = team
        self.team_id = team_id
        self.minutes = float(minutes)
        self.pts = int(stats[0])
        self.dreb = int(stats[1])
        self.oreb = int(stats[2])
        self.reb = self.oreb + self.dreb
        self.ast = int(stats[3]) 
        self.stl = int(stats[4])
        self.blk = int(stats[5])
        self.tov = int(stats[6])  
        self.fgm = int(stats[7])
        self.fga = int(stats[8])
        self.fg3m = int(stats[9])
        self.fg3a = int(stats[10])
        self.ftm = int(stats[11])
        self.fta = int(stats[12])
        self.pfoul = int(stats[13])
        
        self.game_score = self.pts + (0.4*self.fgm) - (0.7*self.fga) - (0.4)*(self.fta - self.ftm) + (0.7*self.oreb) + (0.3*self.dreb) + self.stl + (0.7*self.ast) + (0.7*self.blk) - (0.4*self.pfoul) - self.tov

    def __str__(self):
        return """{} - {}: PTS: {}   REB: {}   AST: {}   BLK: {}   STL: {}   TOV: {}   MIN: {:.1f}   {}/{} FG   {}/{} 3FG   {}/{} FT\n""".format(self.team, self.name, self.pts, self.reb, self.ast, self.blk, self.stl, self.tov, self.minutes, self.fgm, self.fga, self.fg3m, self.fg3a, self.ftm, self.fta) 
