"""Модуль отвечает за 'выдёргивание' имён команд из HTML"""

def returnNameTeam(match):
  """Возвращает имена играющих команд 
    Возвращаемое значение - ('Дома', 'Гости')
    Принимаемое значение - объект BS 
  """
  homeName = match.find('div', class_='event__participant--home').text
  awayName = match.find('div', class_='event__participant--away').text
  return homeName, awayName 