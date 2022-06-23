"""Модуль, отвечающий за 'определение' победителя на основе листов 
со значениями набранных очков по четвертям"""

def calcResult(*team):
  """Получает кортеж с двумя листами и вызывает MaxPointInTime"""
  # team -> ([25, 29, 39, 25], [28, 34, 14, 31])
  homePoint, alowePoint = team
  winnerList = []
  for i in range(len(homePoint)): 
    if homePoint[i] > alowePoint[i]: 
      winnerList.append('home')
    else: 
      winnerList.append('alowe')
  
  if winnerList[0] == winnerList[1]:
    if winnerList[0] != winnerList[2]:
      return f'Заход_3'
    elif winnerList[0] != winnerList[3]:
      return f'Заход_4'
    else:
      return f'Поражение'
  else: 
    return f'Не подошёл'