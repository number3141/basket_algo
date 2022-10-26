import pandas

from data.saveData import saveData


class MatchList():
    def __init__(self, listObj = []) -> None:
        self.dataList = listObj
        self.dataListWithStructForWriting = []
        self.columns = ['Дата', "Команды", "1", '2', '3', '4', 'Итог']

    def __repr__(self) -> str:
        return f'Матч-лист {self.frame}'

    def addMatchInList(self, match):
        self.dataList.append(match) 

    def fillDataFrameBeforeSave(self):
        for item in self.dataList: 
            homeTeam = [item['matchDate'], item['nameHome'], *item['pointHome'], item['result']]
            awayTeam = [item['matchDate'], item['nameAway'], *item['pointAway'], item['result']]
            self.dataListWithStructForWriting.append(homeTeam)
            self.dataListWithStructForWriting.append(awayTeam)
            
            