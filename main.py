from unittest.mock import patch
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox

from data import Connection, FrequencyList, Match, MatchList, SoupFromHTML
from data.saveData import saveData
from display import Window


class StartWindow(Window): 
    
    def startProgram(self):
        self.getWebPageContent()
        self.startCookedSoupFromSite()
        self.calculateResultAllMatches()
    
    def getWebPageContent(self) -> None: 
        """Соединяемся с сайтом и забирам весь контент с него"""
        self.webpage = Connection('https://www.flashscore.ru.com/basketball/usa/nba/results/')
        self.pageContent = self.webpage.getContent()
            
    def startCookedSoupFromSite(self) -> None: 
        """Создание супа из сайта"""
        inputDate = self.date.text()
        self.soup = SoupFromHTML(inputDate, self.pageContent)
        
    def calculateResultAllMatches(self): 
        self.allMatches = self.soup.returnAllFoundMatches()
        self.matchList = MatchList()
        self.freqList = FrequencyList()
        for item in self.allMatches: 
            newMatch = Match(item)
            newMatch.calcResult()
            self.freqList.addTeamInList(newMatch.getNameTeam())
            self.matchList.addMatchInList(newMatch.getData())
            self.fillTable(newMatch.getData())
        self.fillFreqTable(self.freqList.getData())
        print('Готово!')

    def saveInFile(self, path):
        rows = self.table.rowCount()
        if not rows:
            QMessageBox.information(self, 'Внимание', 'Нечего сохранять.')
            return  
        path = QFileDialog.getSaveFileName(self, 'Save Excel', '.', 'XLSX(*.xlsx)')
        if not path:
            QMessageBox.information(self, 'Внимание', 'Не указан файл для сохранения.')
            return
        
        self.matchList.fillDataFrameBeforeSave()
        self.freqList.fillDataFrameBeforeSave()

        saveMatches = saveData()
        saveMatches.addFrame(self.matchList.dataListWithStructForWriting, self.matchList.columns, 'MatchList')
        saveMatches.addFrame(self.freqList.freqListWithStructForWriting, self.freqList.columns, 'FreqList')
        
        saveMatches.saveInExcel(path[0])
        
        QMessageBox.information(self, 'Успешно', 'Файл успешно сохранён')


def startApp(): 
    app = QApplication([])
    # Исп. как контейнер 
    window = StartWindow()
    window.show()
    app.exec_()

if __name__ == '__main__': 
    startApp()
