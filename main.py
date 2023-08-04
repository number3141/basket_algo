# from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox

from data import Connection_Selenium, Interface_Scraper_HTML, FrequencyList, MatchBasket, MatchListBasket, SoupFromHTML, SaveData
from display import GraphInterface, save_user_settings, load_user_settings

import dearpygui.dearpygui as dpg
import time


class MainProgram(GraphInterface): 
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
        self.basket_connection = Connection_Selenium('https://www.flashscorekz.com/basketball/usa/nba/results/')
        self.basket_connection.start_connect()
        self.scrap_interface = Interface_Scraper_HTML()


    def startCookedSoupFromSite(self) -> None: 
        """Создание супа из сайта"""
        self.pageContent = self.scrap_interface.get_result_flashcsore(self.basket_connection, self.inputDate)   
        self.soup = SoupFromHTML(self.inputDate, self.pageContent)
        self.basket_connection.close_connect()
        

    def calculateResultAllMatches(self): 
        self.allMatches = self.soup.returnAllFoundMatches()
        self.matchList = MatchListBasket()
        self.freqList = FrequencyList()

        for item in self.allMatches: 
            newMatch = MatchBasket(item)
            newMatch.calcResult()

            if newMatch.isAppropriateMatch():          
                self.freqList.addTeamInList(newMatch)

            self.matchList.addMatchInList(newMatch)
            self.fillTable(newMatch)
        
        self.fillFreqTable(self.freqList.getData())


    def save_in_file(self, path):
        "Сохраняет таблицы в файл"
        path =  dpg.get_value(item='save_path')

        if not path:
            dpg.add_text(tag='error_data', default_value='Не указан путь!', before='main_table')
            time.sleep(1)
            dpg.delete_item(item='error_data')
        else: 

            self.matchList.fillDataFrameBeforeSave()
            self.freqList.fillDataFrameBeforeSave()

            saveMatches = SaveData()
            saveMatches.addFrame(self.matchList.dataListWithStructForWriting, self.matchList.columns, 'MatchList')
            saveMatches.addFrame(self.freqList.freqListWithStructForWriting, self.freqList.columns, 'FreqList')
            saveMatches.saveInExcel(path)
            print('Сохранил!')

    
    def save_settings(self):
        user_data = {
            'save_path': dpg.get_value('save_path')
        }
        save_user_settings(user_data)



def startApp(): 
    window = MainProgram()

if __name__ == '__main__':
    startApp()

