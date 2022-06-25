from itertools import count
from operator import index
from data import returnAllFoundMatches, returnNameTeam, cutPoint, calcResult
# from display import saveCountTeamInExcel
from display import saveResultInExcel, parsePageInHTML, Window
from PyQt5.QtWidgets import QApplication, QTableWidgetItem

class StartWindow(Window): 

  def fillTable(self, names, pointList, resultList): 
      countRow = self.table.rowCount()
      isSecondTeam = 0
      for indexRow in range(countRow, countRow + 2): 
        self.table.insertRow(indexRow)
        self.table.setItem(indexRow, 1, QTableWidgetItem(names[isSecondTeam]))
        for period in range(4): 
          self.table.setItem(indexRow, period + 2, QTableWidgetItem(str(pointList[isSecondTeam][period])))
        self.table.setItem(indexRow, 6, QTableWidgetItem(str(resultList)))
        isSecondTeam = 1

  def startProgram(self): 
    # Парсим страницу в HTML
    parsePageInHTML()
    date = self.date.text()
    allMatch = returnAllFoundMatches(date)
    for item in allMatch: 
      pointList = cutPoint(item)
      names = returnNameTeam(item)
      winnerList = calcResult(*pointList)
      self.fillTable(names, pointList, winnerList)
      # saveResultInExcel(names, point, winnerList)
    # self.close()
    print('Готово!')


def startApp(): 
    app = QApplication([])
    # Исп. как контейнер 
    window = StartWindow()
    window.show()
    app.exec_()

if __name__ == '__main__': 
  startApp()

  