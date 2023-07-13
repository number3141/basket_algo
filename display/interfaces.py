import dearpygui.dearpygui as dpg

from .setup import load_user_settings

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300, clear_color=(192,192,192,255))


class GraphInterface(): 
    def __init__(self) -> None:
        #  Установка шрифта
        with dpg.font_registry():
            with dpg.font("./LiteralRegular.otf", 18, default_font=True, tag="Default font") as f:
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

        with dpg.window(label="Example Window", width=1000, height=500, tag='main_wind'):
            with dpg.tab_bar():
                # Главная страница 
                with dpg.tab(label='Main'):
                    # Кнопки поиска и ввода даты
                    with dpg.group():
                        dpg.add_text(default_value="Last Date")
                        with dpg.group(horizontal=True):   
                            dpg.add_input_text(tag='date_user', no_spaces = True, decimal= True, width=100)
                            dpg.add_button(label="Поиск матчей", callback=self.start_program)
                            dpg.add_button(label="Сохранить!", callback=self.save_in_file)
                    # Таблица команд
                    with dpg.table(tag = 'main_table'):
                        dpg.add_table_column(label='Дата')
                        dpg.add_table_column(label='Команда')
                        dpg.add_table_column(label='1 четверть')
                        dpg.add_table_column(label='2 четверть')
                        dpg.add_table_column(label='3 четверть')
                        dpg.add_table_column(label='4 четверть')
                        dpg.add_table_column(label='Итог')
                    # Таблица частоты
                    with dpg.table(tag = 'freq_table'):
                        dpg.add_table_column(label='Команда')
                        dpg.add_table_column(label='Отдали четверть после половины')
                        dpg.add_table_column(label='Забрали четверть после половины')
                        dpg.add_table_column(label='Проиграли по страте')
                        dpg.add_table_column(label='Всего')

                # Страница настроек 
                with dpg.tab(label='Settings'): 
                    dpg.add_input_text(label='Путь сохранения', tag = 'save_path', default_value='')
                    dpg.add_button(label='Сохранить настройки', tag = 'bth_save_settings', callback=self.save_settings)

            dpg.show_item_registry()
            dpg.bind_font("Default font")
            dpg.set_primary_window(window='main_wind', value=True)

            self.load_settings()

            dpg.setup_dearpygui()
            dpg.show_viewport()
            dpg.start_dearpygui()
            dpg.destroy_context()
      

    def fillTable(self, match): 
        """
        Функция-обёртка, которая поочерёдно сохраняет данные для каждой команды в матче 

        Аргументы 
            ----------
            - match (dict) - словарь с данными, которые будут добавлены в таблицу  
        """
        home_team_name = match.get_name_home_team()
        away_team_name = match.get_name_away_team()
        points_home = match.get_points_home()
        points_away = match.get_points_away()
        self.createRowsWithMatchData(match, home_team_name, points_home)
        self.createRowsWithMatchData(match, away_team_name, points_away) 


    def createRowsWithMatchData(self, match, team_name, points_team):
        """
        Функия для заполнения таблицы со всеми матчами

        Аргументы
        ----------
        - match (dict) - словарь с данными, которые будут добавлены в таблицу 
        - prefix (str) - строка "Home" или "Away" 
        
        """

        match_date = match.get_match_date()
        match_result = match.get_result_match() 

        with dpg.table_row(parent='main_table'):
            dpg.add_text(match_date)
            dpg.add_text(team_name)
            # Добавление очков (4 четверти)
            dpg.add_text(str(points_team[0]))
            dpg.add_text(str(points_team[1]))
            dpg.add_text(str(points_team[2]))
            dpg.add_text(str(points_team[3]))
            dpg.add_text(match_result)


    def fillFreqTable(self, match): 
            """
            Функция для заполнения таблицы со статистикой по каждой команде 

            Аргументы 
            ----------
            - match (dict) - словарь с данными, которые будут добавлены в таблицу  
            """
            for item in match: 
                with dpg.table_row(parent='freq_table'):
                    dpg.add_text(str(item))
                    dpg.add_text(match[item]['pass'])
                    dpg.add_text(match[item]['take'])
                    dpg.add_text(match[item]['defeat'])
                    dpg.add_text(match[item]['total'])


    def load_settings(self):
        data_settings = load_user_settings()
        print(f"Дата - {data_settings}")
        dpg.set_value(item='save_path', value=data_settings['save_path'])


    def start_program(self): 
        raise NotImplementedError
    

    def save_in_file(self): 
        raise NotImplementedError
    

    def save_settings(self): 
        raise NotImplementedError
    












# from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMainWindow, QTableWidgetItem, QTableWidget, QHeaderView, QComboBox



# class Window(QMainWindow): 
#     def __init__(self): 
#         super().__init__()

#         self.layout = QVBoxLayout()
#         self.setGeometry(0, 0, 1200, 500)

#         self.setWindowTitle('Basket Parse')
        
#         # Введите дату
#         self.dateLabel = QLabel(self)
#         self.dateLabel.move(10, 10)
#         self.dateLabel.setText('Введите дату')

#         self.date = QLineEdit(self)
#         self.date.move(10, 50)
#         self.date.setInputMask('99.99')

#         # Выберите браузер
#         self.check = QComboBox(self)
#         self.check.move(200, 30)
#         self.check.addItems(["Google", "Firefox"])

#         # Кнопка рассчитать 
#         self.startButton = QPushButton(self)
#         self.startButton.move(10, 100)
#         self.startButton.setText('Рассчитать')

#         self.saveButton = QPushButton(self)
#         self.saveButton.move(120, 100)
#         self.saveButton.setText('Сохранить в CSV')

#         self.freqTable = QTableWidget(self)
#         self.freqTable.setGeometry(700, 150, 480, 320) 
#         self.freqTable.setColumnCount(5) 

#         self.freqHeader = self.freqTable.horizontalHeader()    
#         self.freqHeader.setSectionResizeMode(0, QHeaderView.Stretch)

#         self.table = QTableWidget(self)
#         self.table.setGeometry(10, 150, 680, 320) 
#         self.table.setColumnCount(7)  
#         # Настройка ширины ячеек
#         self.header = self.table.horizontalHeader()    
#         self.header.setSectionResizeMode(1, QHeaderView.Stretch)
#         self.header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
#         self.header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
#         self.header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
#         self.header.setSectionResizeMode(5, QHeaderView.ResizeToContents)

#         self.startButton.clicked.connect(self.startProgram)
#         self.saveButton.clicked.connect(self.saveInFile)

#         # Добавление элементов в шаблон 
#         self.layout.addWidget(self.date)
#         self.layout.addWidget(self.dateLabel)
#         self.layout.addWidget(self.startButton)
#         self.layout.addWidget(self.table)
#         self.layout.addWidget(self.check)
#         self.setLayout(self.layout)
    

#     def fillTable(self, match): 
#         self.currentRow = self.table.rowCount()
#         self.createRowsWithMatchData(match, self.currentRow, 'Home')
#         self.currentRow += 1
#         self.createRowsWithMatchData(match, self.currentRow, 'Away') 

#     def createRowsWithMatchData(self, match, indexCurrentRow, prefix):
#         self.table.insertRow(indexCurrentRow)
#         self.table.setItem(indexCurrentRow, 0, QTableWidgetItem(match['matchDate']))
#         self.table.setItem(indexCurrentRow, 1, QTableWidgetItem(match[f'name{prefix}']))
#         for period in range(4): 
#             currentColumn = period + 2
#             self.table.setItem(indexCurrentRow, currentColumn, QTableWidgetItem(str(match[f'point{prefix}'][period])))
#         self.table.setItem(indexCurrentRow, 6, QTableWidgetItem(str(match['result'])))

#     def fillFreqTable(self, match): 
#         self.currentFreqRow = self.freqTable.rowCount()
#         for item in match: 
#             self.freqTable.insertRow(self.currentFreqRow)
#             self.freqTable.setItem(self.currentFreqRow, 0, QTableWidgetItem(str(item)))
#             self.freqTable.setItem(self.currentFreqRow, 1, QTableWidgetItem(str(match[item]['pass'])))
#             self.freqTable.setItem(self.currentFreqRow, 2, QTableWidgetItem(str(match[item]['take'])))  
#             self.freqTable.setItem(self.currentFreqRow, 3, QTableWidgetItem(str(match[item]['defeat'])))  
#             self.freqTable.setItem(self.currentFreqRow, 4, QTableWidgetItem(str(match[item]['total'])))  
    
#     def startProgram(self):
#         # Абстрактная функция - надо реализовать у того, кто наследует 
#         raise NotImplementedError
    
#     def saveInFile(): 
#         raise NotImplementedError

if __name__ == '__main__': 
    window = Window()