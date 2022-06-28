from data import returnAllFoundMatches, returnNameTeam, cutPoint, calcResult, findMatchData, Match
from data.match import MatchListWrite
from display import parsePageInHTML, Window
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QFileDialog, QMessageBox, QPushButton

matchList = []

class StartWindow(Window): 

  def startProgram(self): 
    global matchList
    
    parsePageInHTML()
    inputDate = self.date.text()
    allMatch = returnAllFoundMatches(inputDate)

    for item in allMatch: 
      matchData = findMatchData(item)
      names = returnNameTeam(item)
      teamPoints = cutPoint(item)
      result = calcResult(teamPoints)

      newMatch = Match(names, teamPoints, matchData, result)
      matchList.append(newMatch.getData())
      self.fillTable(newMatch.getData())
    print('Готово!')

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

  