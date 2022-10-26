import pandas


class MatchList():
    def __init__(self, listObj = []) -> None:
        self.dataList = listObj
        self.dataListWithStructForWriting = []

    def __repr__(self) -> str:
        return f'Матч-лист {self.frame}'

    def addMatchInList(self, match):
        self.dataList.append(match)

    def saveResultInExcel(self, path):
        self.fillDataFrameBeforeSave()
        self.frame = pandas.DataFrame(self.dataListWithStructForWriting, columns=['Дата', "Команды", "1", '2', '3', '4', 'Итог'])
        fileWrite = open(path, 'a', encoding='UTF-8', newline='')
        self.frame.to_csv(fileWrite, index=False, sep=';')

    def fillDataFrameBeforeSave(self):
        for item in self.dataList: 
            homeTeam = [item['matchDate'], item['nameHome'], *item['pointHome'], item['result']]
            awayTeam = [item['matchDate'], item['nameAway'], *item['pointAway'], item['result']]
            self.dataListWithStructForWriting.append(homeTeam)
            self.dataListWithStructForWriting.append(awayTeam)