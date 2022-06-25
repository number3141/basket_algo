"""Модуль, отвечающий за извлечение даты матча"""


def findMatchData(match):
  """Извлекает дату матча из объекта BS4"""
  data = match.find('div', class_='event__time').text
  return str(data) 