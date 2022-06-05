import pandas 

fileTeam = pandas.read_excel(io='./teams.xlsx', engine='openpyxl')

team = fileTeam['Команды']
result = fileTeam['Результат']

teamDict = {}

for item in range(len(fileTeam)): 
  if teamDict.get(fileTeam['Команды'][item]): 
    if any([fileTeam['Результат'][item] == 'Заход_3', fileTeam['Результат'][item] == 'Заход_4']):
      teamDict[fileTeam['Команды'][item]] += 1
  else: 
    teamDict[fileTeam['Команды'][item]] = 1


# Сортировка массива 

sortedKey = sorted(teamDict, key=teamDict.get)

sortedTeam = {}

for item in sortedKey:
  sortedTeam[item] = teamDict[item]

print(sortedTeam) 