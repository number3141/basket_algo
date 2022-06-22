import re
import pandas
from findItem import returnAllFoundMatches
from parseInHTML import parsePageInHTML
# Парсим страницу в HTML
parsePageInHTML()

def cutPoint(match): 
  """Получает один матч и возвращает очки хозяев и гостей
    Возвращаемое значение - ([очки хозяев], [очки гостей])
  """  
  reg = re.compile('\d{2}')
  partHome = []
  partAway = []
  # второй индекс не включается 
  for index in range(1, 5): 
    partPeriodHome = match.select('.event__part--home' + f'.event__part--{index}')
    # Конверт в строку, потому что тип - ResultSet бьютифушный 
    newNum = reg.findall(str(partPeriodHome))
    partHome.append(int(*newNum))

    partPeriodAway = match.select('.event__part--away' + f'.event__part--{index}')
    # Конверт в строку, потому что тип - ResultSet бьютифушный 
    newNum = reg.findall(str(partPeriodAway))
    partAway.append(int(*newNum))
  return partHome, partAway 

def nameTeam(match):
  """Возвращает имена играющих команд 
    Возвращаемое значение - ('Дома', 'Гости')
  """
  homeTeam = match.find('div', class_='event__participant--home').text
  awayTeam = match.find('div', class_='event__participant--away').text
  return homeTeam, awayTeam 

def calcResult(*team):
  """Получает кортеж с двумя листами и вызывает MaxPointInTime"""
  # team -> ([25, 29, 39, 25], [28, 34, 14, 31])
  homePoint, alowePoint = team
  winnerList = winnerInTime(homePoint, alowePoint)
  if winnerList[0] == winnerList[1]:
    if winnerList[0] != winnerList[2]:
      return f'Заход_3'
    elif winnerList[0] != winnerList[3]:
      return f'Заход_4'
    else:
      return f'Поражение'
  else: 
    return f'Не подошёл'

def winnerInTime(home, alowe): 
  """Определяет победителя в каждом тайме
    Возвращаемое значение - ['home', 'home', 'alowe', 'alowe']
  """
  winnerList = []
  for i in range(len(home)): 
    if home[i] > alowe[i]: 
      winnerList.append('home')
    else: 
      winnerList.append('alowe')
  return winnerList

# Сохранение файлов в Excel 
def saveToExcel(nameList, pointList, result):
  oldAr = pandas.read_excel('./teams.xlsx')
  data = pandas.DataFrame({
    'Дата': ['30.05.2022', '0'],
    'Команды':[nameList[0], nameList[1]],
    '1':[pointList[0][0], pointList[1][0]], 
    '2':[pointList[0][1], pointList[1][1]], 
    '3':[pointList[0][2], pointList[1][2]], 
    '4':[pointList[0][3], pointList[1][3]], 
    'Результат': [str(result), str(result)]
  })
  new = pandas.concat([oldAr, data], ignore_index=True)
  new.to_excel('./teams.xlsx', index=False)
  print(pointList)

allMatch = returnAllFoundMatches()

for item in allMatch: 
  point = cutPoint(item)
  names = nameTeam(item)
  winnerList = calcResult(*point)
  saveToExcel(names, point, winnerList)

print('Готово!')