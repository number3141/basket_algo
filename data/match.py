import random
from numpy import append
import pandas

class Match: 
  def __init__(self, nameList, pointList, date, result):
    self.data = {
      # 'id': round(random.random() * 100000), 
      'matchDate': date, 
      'nameHome': nameList[0], 
      'nameAway': nameList[1],
      'pointHome': [pointList['home'][0], pointList['home'][1], pointList['home'][2], pointList['home'][3]], 
      'pointAway': [pointList['away'][0], pointList['away'][1], pointList['away'][2], pointList['away'][3]],
      'result': result
    }

  def getData(self): 
    return self.data

  def __repr__(self) -> str:
    return f"Матч №{self.data['id']} с участием команд {self.data['nameHome']} и {self.data['nameAway']}"


class MatchListWrite():
  def __init__(self, listObj) -> None:
    self.dataList = listObj
    self.listForWrite = []

  def __repr__(self) -> str:
    return f'Матч-лист {self.frame}'

  def saveResultInExcel(self, path):
    self.fillDataFrameBeforeSave()
    self.frame = pandas.DataFrame(self.listForWrite, columns=['Дата', "Команды", "1", '2', '3', '4', 'Итог'])
    fileWrite = open(path, 'a', encoding='UTF-8', newline='')
    self.frame.to_csv(fileWrite, index=False, sep=';')

  def fillDataFrameBeforeSave(self):
    for item in self.dataList: 
      homeTeam = [item['matchDate'], item['nameHome'], *item['pointHome'], item['result']]
      awayTeam = [item['matchDate'], item['nameAway'], *item['pointAway'], item['result']]
      self.listForWrite.append(homeTeam)
      self.listForWrite.append(awayTeam)

  



if __name__ == '__main__': 
  newMatch = Match(['Бостон', 'Маверикс'], [[5, 6, 3, 4], [1, 4, 2, 5]], '12.04 08:00', 'Заход_3')
  newMatch2 = Match(['Даллас', 'Детроит'], [[7, 2, 3, 8], [6, 4, 5, 1]], '12.04 10:00', 'Заход_4')

  matchList = MatchListWrite([newMatch.getData(), newMatch2.getData()])

  matchList.fillDataFrameBeforeSave()