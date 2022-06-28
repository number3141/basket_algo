"""Модуль, отвечающий за 'определение' победителя на основе листов 
со значениями набранных очков по четвертям"""

def calcResult(teamPoints):
  """Получает словарь с очками команд и проверяет победителя в каждой четверти"""
  # team -> ([25, 29, 39, 25], [28, 34, 14, 31])
  homePoint = teamPoints['home']
  alowePoint = teamPoints['away']
  winnerList = []
  for i in range(len(homePoint)): 
    if homePoint[i] > alowePoint[i]: 
      winnerList.append('home')
    else: 
      winnerList.append('away')
  
  if winnerList[0] == winnerList[1]:
    if winnerList[0] != winnerList[2]:
      return f'Заход_3'
    elif winnerList[0] != winnerList[3]:
      return f'Заход_4'
    else:
      return f'Поражение'
  else: 
    return f'Не подошёл'