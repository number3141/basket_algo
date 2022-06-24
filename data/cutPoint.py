"""Модуль, отвечающий за извлечение очков команд из BS"""
import re

def cutPoint(match): 
  """Получает один матч и возвращает очки хозяев и гостей
    Возвращаемое значение - ([очки хозяев], [очки гостей])
  """  
  partHome = []
  partAway = []
  for part in range(1, 5): 
    partPeriodHome = selectPointInPartByPlayField(match, 'home', part)
    partHome.append(findDecimalNumImStr(partPeriodHome))
    partPeriodAway = selectPointInPartByPlayField(match, 'away', part)
    partAway.append(findDecimalNumImStr(partPeriodAway))
  return partHome, partAway 


def selectPointInPartByPlayField(match, playField, part):
  return match.select(f'.event__part--{playField}' + f'.event__part--{part}')

def findDecimalNumImStr(findStr):
   # Регулярная строка для поиска всех десятичных чисел 
  reg = re.compile('\d{2}')
  # Конверт в строку, потому что тип - ResultSet бьютифушный 
  findPointInPart = reg.findall(str(findStr))
  return int(*findPointInPart)
