import pandas 

def saveResultInExcel(nameList, pointList, result, path):
  """Принимает 
    nameList - ['Team', 'Team'], 
    pointList - [[10, 11, 12, 13], [5, 4, 3, 2]], 
    result - 'итог'
    И сохраняет в Excel
  """
  oldAr = pandas.read_excel(path, engine='openpyxl')
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
  new.to_excel(path, index=False)
  print(pointList)
