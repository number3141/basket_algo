from data import returnAllFoundMatches, returnNameTeam, cutPoint, calcResult
# from display import saveCountTeamInExcel
from display import saveResultInExcel, parsePageInHTML, Window
from PyQt5.QtWidgets import QApplication

class StartWindow(Window): 
  def startProgram(self): 
    # Парсим страницу в HTML
    parsePageInHTML()
    date = self.date.text()
    allMatch = returnAllFoundMatches(date)
    for item in allMatch: 
      point = cutPoint(item)
      names = returnNameTeam(item)
      winnerList = calcResult(*point)
      saveResultInExcel(names, point, winnerList)
    self.close()
    print('Готово!')

def startApp(): 
    app = QApplication([])
    # Исп. как контейнер 
    window = StartWindow()
    window.show()
    app.exec_()

if __name__ == '__main__': 
  startApp()

  