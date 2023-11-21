import csv
import json
import dearpygui.dearpygui as dpg

from user_interface.interface import Interface


class GraphInterface(Interface): 
    def __init__(self) -> None:
        self.data = self.load_settings()
        dpg.create_context()
        dpg.create_viewport(title='Basket Parse', width=900, height=600, clear_color=(192,192,192,255))


    def draw_main_window(self, start_programm, save_match, save_freq): 

        # Нет поддержки кириллицы в сборке  
        # with dpg.font_registry():
        #     with dpg.font("./LiteralRegular.otf", 18, default_font=True, tag="Default font") as f:
        #         dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

        with dpg.window(label="Example Window", width=1000, height=500, tag='main_wind'):
            with dpg.tab_bar():
                # Главная страница 
                with dpg.tab(label='Main', tag='main'):
                    # Кнопки поиска и ввода даты
                    with dpg.group():
                        dpg.add_text(default_value="Input Date")
                        with dpg.group(horizontal=True):   
                            dpg.add_input_text(tag='date_user', no_spaces = True, decimal=True, width=100)
                            dpg.add_button(label="Search", callback=lambda x: start_programm(user_data = dpg.get_value('date_user')))
                            dpg.add_button(label="Save MatchTable", callback=save_match)
                            dpg.add_button(label="Save FreqTable", callback=save_freq)
                        
                    # Таблица команд
                    with dpg.table(tag = 'main_table'):
                        dpg.add_table_column(label='Date')
                        dpg.add_table_column(label='TeamName')
                        dpg.add_table_column(label='1 part')
                        dpg.add_table_column(label='2 part')
                        dpg.add_table_column(label='3 part')
                        dpg.add_table_column(label='4 part')
                        dpg.add_table_column(label='Result')
                    # Таблица частоты
                    with dpg.table(tag = 'freq_table'):
                        dpg.add_table_column(label='Team')
                        dpg.add_table_column(label='Apropriate Match')
                        dpg.add_table_column(label='All Match')

                # Страница настроек 
                with dpg.tab(label='Settings'): 
                    with dpg.group():
                        dpg.add_text('Name MatchTable File')
                        dpg.add_input_text(tag='match_name', default_value=self.data['name_match_table'])

                    with dpg.group():
                        dpg.add_text('Name FreqTable File')
                        dpg.add_input_text(tag='freq_name', default_value=self.data['name_freq_table'])
                    
                    dpg.add_button(label='Save Settings', tag='bth_save_settings', callback=self.save_settings)


            dpg.bind_font("Default font")
            dpg.set_primary_window(window='main_wind', value=True)

            dpg.setup_dearpygui()
            dpg.show_viewport()
            dpg.start_dearpygui()
            dpg.destroy_context()
      

    def draw_match_table(self, match_list:dict):
        """
        Функия для заполнения таблицы со всеми матчами

        Аргументы
        ----------
        - match (dict) - словарь с данными, которые будут добавлены в таблицу 
        - preffix - home или away 
        """

        for match in match_list: 
            for preffix in ['home', 'away']: 
                with dpg.table_row(parent='main_table'):
                    dpg.add_text(match['date'])
                    dpg.add_text(match[f'name_{preffix}'])
                    # Добавление очков (4 четверти)
                    dpg.add_text(str(match[f'points_{preffix}'][0]))
                    dpg.add_text(str(match[f'points_{preffix}'][1]))
                    dpg.add_text(str(match[f'points_{preffix}'][2]))
                    dpg.add_text(str(match[f'points_{preffix}'][3]))
                    dpg.add_text(str(match['is_inderhand']))


    def draw_freq_table(self, freq_list): 
            """
            Функция для заполнения таблицы со статистикой по каждой команде 

            Аргументы 
            ----------
            - match (dict) - словарь с данными, которые будут добавлены в таблицу  
            """
            for team_name_key in freq_list: 
                with dpg.table_row(parent='freq_table'):
                    dpg.add_text(team_name_key)
                    dpg.add_text(freq_list[team_name_key]['aprop_match'])
                    dpg.add_text(freq_list[team_name_key]['all_match'])
    

    def save_match_list(self, match_list):
        file_name = dpg.get_value('match_name')
        # Если csvfile является файловым объектом, то его нужно открыть с параметром newline=''
        with open(file_name, 'w', encoding='UTF-8', newline='') as f:
            # Разделитель запятая не разбивает на колонки 
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['Дата', "Дома", "Гости", "Очки дома", "Очки гостей", "Результат"])
            # writer = csv.DictWriter(f, fieldnames = match_list[0].keys(), delimiter=';')
            # writer.writeheader()
            
            for match in match_list: 
                writer.writerow(match.values())


    def save_freq_list(self, freq_list):
        file_name = dpg.get_value('freq_name')
        # Если csvfile является файловым объектом, то его нужно открыть с параметром newline=''
        with open(file_name, 'w', encoding='UTF-8', newline='') as f:
            # Разделитель запятая не разбивает на колонки 
            writer = csv.writer(f, delimiter=';')
            writer.writerow(["Название", "Матчей подошло", "Матчей всего сыграно"])
            # writer = csv.DictWriter(f, fieldnames = match_list[0].keys(), delimiter=';')
            # writer.writeheader()
            
            for match in freq_list: 
                writer.writerow([match, *freq_list[match].values()]) 


    def save_settings(self):  
        my_dict = {
            'name_match_table': dpg.get_value('match_name'), 
            'name_freq_table': dpg.get_value('freq_name'), 
        }
        
        with open('settings.json', 'w') as f:
            json.dump(my_dict, f)


    def load_settings(self): 
        with open('settings.json', 'a+') as f:
            text = f.read()
            if len(text) < 1: 
                return {
                    'name_match_table': 'match_name.csv', 
                    'name_freq_table': 'freq_name.csv', 
                }
            else:
                return json.load(f) 


        
    def draw_text_in_board(self, message): 
        with dpg.group(parent='main', tag='alert_group', horizontal=True):
            dpg.add_text(default_value=message)
            dpg.add_button(label='Закрыть', callback=lambda x: dpg.delete_item(item='alert_group'))
