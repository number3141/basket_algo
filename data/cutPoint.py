"""Модуль, отвечающий за извлечение очков команд из BS"""
import re

def cutPoint(match): 
  """Получает один матч и возвращает очки хозяев и гостей
    Возвращаемое значение - ([очки хозяев], [очки гостей])
  """  
  parts = {
    'home': [],
    'away': []
  }
  for part in range(1, 5): 
    partPeriodHome = selectPointInPartByPlayField(match, 'home', part)
    parts['home'].append(findDecimalNumImStr(partPeriodHome))
    partPeriodAway = selectPointInPartByPlayField(match, 'away', part)
    parts['away'].append(findDecimalNumImStr(partPeriodAway))
  return parts


def selectPointInPartByPlayField(match, playField, part):
  return match.select(f'.event__part--{playField}' + f'.event__part--{part}')

def findDecimalNumImStr(findStr):
   # Регулярная строка для поиска всех десятичных чисел 
  reg = re.compile('\d{2}')
  # Конверт в строку, потому что тип - ResultSet бьютифушный 
  findPointInPart = reg.findall(str(findStr))
  return int(*findPointInPart)
