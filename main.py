from data import returnAllFoundMatches, returnNameTeam, cutPoint, calcResult, findMatchData, Match, MatchListWrite
from display import Window
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox

from display.parseInHTML import SoupFromHTML

matchList = []

class StartWindow(Window): 

  def startProgram(self): 
    global matchList
    soup = SoupFromHTML('https://www.flashscore.com.ua/basketball/usa/nba/results/').getSoup()
    inputDate = self.date.text()
    allMatch = returnAllFoundMatches(inputDate, soup)

    for item in allMatch: 
      matchData = findMatchData(item)
      names = returnNameTeam(item)
      teamPoints = cutPoint(item)
      result = calcResult(teamPoints)

      newMatch = Match(names, teamPoints, matchData, result)
      matchList.append(newMatch.getData())
      self.fillTable(newMatch.getData())
    print('Готово!')

  def saveInFile(self, path):
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
    QMessageBox.information(self, 'Успешно', 'Файл успешно сохранён')


def startApp(): 
    app = QApplication([])
    # Исп. как контейнер 
    window = StartWindow()
    window.show()
    app.exec_()

if __name__ == '__main__': 
  startApp()

  