from data import returnAllFoundMatches, returnNameTeam, cutPoint, calcResult
# from display import saveCountTeamInExcel
from display import saveResultInExcel, parsePageInHTML

if __name__ == '__main__': 
  # Парсим страницу в HTML
  parsePageInHTML()

  allMatch = returnAllFoundMatches()
  for item in allMatch: 
    point = cutPoint(item)
    names = returnNameTeam(item)
    winnerList = calcResult(*point)
    saveResultInExcel(names, point, winnerList)

  print('Готово!')