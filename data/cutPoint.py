"""Модуль, отвечающий за извлечение очков команд из BS"""
import re

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
    newNum = reg.findall(str(partPeriodAway))
    partAway.append(int(*newNum))
  return partHome, partAway 