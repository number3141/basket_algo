from data import returnAllFoundMatches, Match, MatchList
from display import Window, SoupFromHTML
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
class StartWindow(Window): 
  def startProgram(self): 
    soup = SoupFromHTML('https://www.flashscore.com.ua/basketball/usa/nba/results/').getSoup()
    inputDate = self.date.text()
    allMatch = returnAllFoundMatches(inputDate, soup)
    self.matchList = MatchList()
    for item in allMatch: 
      newMatch = Match(item)
      newMatch.calcResult()
      self.matchList.addMatchInList(newMatch.getData())
      self.fillTable(newMatch.getData())
    print('Готово!')

  def saveInFile(self, path):
    rows = self.table.rowCount()
    if not rows:
      QMessageBox.information(self, 'Внимание', 'Нечего сохранять.')
      return  
    path, _ = QFileDialog.getSaveFileName(self, 'Save CSV', '.', 'CSV(*.csv)')
    if not path:
      QMessageBox.information(self, 'Внимание', 'Не указан файл для сохранения.')
      return
    self.matchList.saveResultInExcel(path)
    QMessageBox.information(self, 'Успешно', 'Файл успешно сохранён')


def startApp(): 
    app = QApplication([])
    # Исп. как контейнер 
    window = StartWindow()
    window.show()
    app.exec_()

if __name__ == '__main__': 
  startApp()

  