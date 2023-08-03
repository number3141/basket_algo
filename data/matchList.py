class MatchList():
    def __init__(self, listObj = []) -> None:
        self.dataList = listObj
        self.dataListWithStructForWriting = []
        

    def __repr__(self) -> str:
        return f'Матч-лист {self.dataList}'
      
            
class MatchListBasket(MatchList): 
    def __init__(self, listObj=[]) -> None:
        super().__init__(listObj)
        self.columns = ['Дата', "Команды", "1", '2', '3', '4', 'Итог']


    def addMatchInList(self, match):
        self.dataList.append(match) 


    def fillDataFrameBeforeSave(self):
        for item in self.dataList: 

            match_date = item.get_match_date()
            home_team_name = item.get_name_home_team()
            away_team_name = item.get_name_home_team()
            points_home = item.get_points_home()
            points_away = item.get_points_away()
            match_result = item.get_result_match() 

            homeTeam = [match_date, home_team_name, *points_home, match_result]
            awayTeam = [match_date, away_team_name, *points_away, match_result]
            self.dataListWithStructForWriting.append(homeTeam)
            self.dataListWithStructForWriting.append(awayTeam)