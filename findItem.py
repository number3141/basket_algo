from bs4 import BeautifulSoup

def decData(date) -> str:
  """Уменьшает дату и возвращает обновлённую строку"""
  zeroBeforeDay = zeroBeforeMonth = ''
  dataList = [int(x) for x in date.split('.')]
  month = dataList[1]
  day = dataList[0]

  if day == 1:
    month -= 1
    day = 31
    if month < 1: 
      month = 12
  else: 
    day -= 1

  if month <= 9: 
    zeroBeforeMonth = '0'
  if day <= 9: 
    zeroBeforeDay = '0'
  return f'{zeroBeforeDay}{day}.{zeroBeforeMonth}{month}'

def findStopMatch(data, html):
  """Получает дату и находит последний матч, перебирая все времена, в которых играют команды"""
  timeList = ['01:00', '01:30', '02:30', '02:30', '03:00', '03:30', '04:00', '04:30', '05:00',
   '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30']
  for time in timeList: 
    # Первый родитель - блок data, второй - само событие. Поэтому parent.parent
    try: 
      print(f"{data}. {time}")
      stopMatch = html.find(string=f"{data}. {time}").parent.parent
      if stopMatch: 
        return stopMatch
    except: 
      continue

def returnAllFoundMatches():
  fileBask = open('bask.html', 'r', encoding='utf-8')
  soup = BeautifulSoup(fileBask, 'lxml')
  userData = input('Введите дату в формате XX.XX (31.12)')
  while True: 
    """Пока не найдёт ближайшие матчи - будет уменьшать дату"""
    stopMatch = findStopMatch(userData, soup)
    # print(f'Проверяю матч с датой {userData}')
    if stopMatch: 
      # Склеенный массив 
      findMatch = [stopMatch] + list(stopMatch.find_all_previous('div', class_ = 'event__match'))
      return findMatch
    else: 
      userData = decData(userData)  
    
    