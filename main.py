from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox

from data import Connection, FrequencyList, Match, MatchList, SoupFromHTML, SaveData
from display import Window


class StartWindow(Window): 
    
    def startProgram(self):
        self.getWebPageContent()
        self.startCookedSoupFromSite()
        self.calculateResultAllMatches()
    

    def getWebPageContent(self) -> None: 
        """Соединяемся с сайтом"""
        browser = self.check.currentText()
        self.webpage = Connection('https://www.flashscorekz.com/basketball/usa/nba/results/', browser)
        

    def startCookedSoupFromSite(self) -> None: 
        """Создание супа из сайта"""
        self.pageContent = self.webpage.getContent()

        inputDate = self.date.text()
        self.soup = SoupFromHTML(inputDate, self.pageContent)
        

    def calculateResultAllMatches(self): 
        self.allMatches = self.soup.returnAllFoundMatches()
        self.matchList = MatchList()
        self.freqList = FrequencyList()

        for item in self.allMatches: 
            newMatch = Match(item)
            newMatch.calcResult()

            if newMatch.isAppropriateMatch():          
                self.freqList.addTeamInList(newMatch.getData())

            self.matchList.addMatchInList(newMatch.getData())
            self.fillTable(newMatch.getData())

        self.fillFreqTable(self.freqList.getData())


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

        saveMatches = SaveData()
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
