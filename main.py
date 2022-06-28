from data import returnAllFoundMatches, returnNameTeam, cutPoint, calcResult, findMatchData, Match
from data.match import MatchListWrite
# from display import saveCountTeamInExcel
from display import saveResultInExcel, parsePageInHTML, Window
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QFileDialog, QMessageBox, QPushButton

matchList = []

class StartWindow(Window): 
  def startProgram(self): 
    global matchList
    # Парсим страницу в HTML
    parsePageInHTML()
    date = self.date.text()
    allMatch = returnAllFoundMatches(date)
    for item in allMatch: 
      matchData = findMatchData(item)
      pointList = cutPoint(item)
      names = returnNameTeam(item)
      result = calcResult(*pointList)
      newMatch = Match(names, pointList, matchData, result)
      matchList.append(newMatch.getData())
      self.fillTable(names, pointList, result, matchData)
    # self.close()
    print('Готово!')
  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  def saveInExcel(self, path):
    global matchList
    rows = self.table.rowCount()
    if not rows:
      QMessageBox.information(self, 'Внимание', 'Нечего сохранять.')
      return  
    path, _ = QFileDialog.getSaveFileName(self, 'Save CSV', '.', 'CSV(*.csv)')
    if not path:
      QMessageBox.information(self, 'Внимание', 'Не указан файл для сохранения.')
      return
    mat = MatchListWrite(matchList)
    mat.saveResultInExcel(path)


def startApp(): 
    app = QApplication([])
    # Исп. как контейнер 
    window = StartWindow()
    window.show()
    app.exec_()

if __name__ == '__main__': 
  startApp()

  