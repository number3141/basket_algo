# from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox

from data import Connection, FrequencyList, Match, MatchList, SoupFromHTML, SaveData
from display import Window, save_user_settings, load_user_settings

import dearpygui.dearpygui as dpg
import time


class StartWindow(Window): 
    """
    Класс, открывающий окно приложения для парсинга

    Методы
    ----------
    startProgram() 
        Вызывает методы .getWebPageContent(), 
        .startCookedSoupFromSite() и calculateResultAllMatches()
    
    getWebPageContent() 
        Открывает соединение с сайтом 

    """        
    def start_program(self):
        self.getWebPageContent()
        self.startCookedSoupFromSite()
        self.calculateResultAllMatches()
    

    def getWebPageContent(self) -> None: 
        """Соединяемся с сайтом"""
        self.inputDate = dpg.get_value('date_user')
        self.webpage = Connection('https://www.flashscorekz.com/basketball/usa/nba/results/', self.inputDate)


    def startCookedSoupFromSite(self) -> None: 
        """Создание супа из сайта"""
        self.pageContent = self.webpage.getContent()    
        self.soup = SoupFromHTML(self.inputDate, self.pageContent)
        

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


    def save_in_file(self, path):
        "Сохраняет таблицы в файл"
        path =  dpg.get_value(item='save_path')

        if not path:
            dpg.add_text(tag='error_data', default_value='Не указан путь!', before='main_table')
            time.sleep(1)
            dpg.delete_item(item='error_data')
        else: 

            # with dpg.popup(parent='main_table', mousebutton=dpg.mvMouseButton_Left,  modal=True, tag="modal_id"):
            #     dpg.add_text('Внимание! Нечего сохранять!')
                # dpg.add_button(label="Close", callback=lambda: dpg.configure_item("modal_id", show=False))

            self.matchList.fillDataFrameBeforeSave()
            self.freqList.fillDataFrameBeforeSave()

            saveMatches = SaveData()
            saveMatches.addFrame(self.matchList.dataListWithStructForWriting, self.matchList.columns, 'MatchList')
            # saveMatches.addFrame(self.freqList.freqListWithStructForWriting, self.freqList.columns, 'FreqList')
            
            saveMatches.saveInExcel(path)
            
            # QMessageBox.information(self, 'Успешно', 'Файл успешно сохранён')
            print('Сохранил!')

    
    def save_settings(self):
        user_data = {
            'save_path': dpg.get_value('save_path')
        }
        save_user_settings(user_data)



def startApp(): 
    # app = QApplication([])
    # Исп. как контейнер 
    window = StartWindow()
    # window.show()
    # app.exec_()

if __name__ == '__main__':
    startApp()

