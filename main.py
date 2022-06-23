import re
from data import parsePageInHTML
from data import returnAllFoundMatches
# from display import saveCountTeamInExcel
from display import saveResultInExcel

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

allMatch = returnAllFoundMatches()

for item in allMatch: 
  point = cutPoint(item)
  names = nameTeam(item)
  winnerList = calcResult(*point)
  saveResultInExcel(names, point, winnerList)

print('Готово!')