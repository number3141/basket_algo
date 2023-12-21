import csv
import json
import dearpygui.dearpygui as dpg

from user_interface.interface import Interface


def save_settings(name):
    file_name = name.replace(' ', '_').replace(',', '_')
    if '.csv' not in file_name:
        file_name += '.csv'

    my_dict = {
        'name_freq_table': file_name,
    }

    with open('settings.json', 'w') as f:
        json.dump(my_dict, f)


def load_settings():
    with open('settings.json', 'r') as f:
        text = json.load(f)
        if len(text) < 1:
            return {
                'name_freq_table': 'freq_name.csv',
            }
        else:
            return text


class GraphInterface(Interface):
    def __init__(self) -> None:
        self.data = load_settings()
        dpg.create_context()
        dpg.create_viewport(title='Basket Parse', width=900, height=600, clear_color=(192, 192, 192, 255))

    def draw_main_window(self, start_programm, save_freq):

        # Нет поддержки кириллицы в сборке  
        with dpg.font_registry():
            with dpg.font("./LiteralRegular.otf", 20, default_font=True, tag="Default font") as f:
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

        with dpg.window(label="Example Window", width=1000, height=500, tag='main_wind'):
            with dpg.tab_bar():
                # Главная страница 
                with dpg.tab(label='Main', tag='main'):
                    # Кнопки поиска и ввода даты
                    with dpg.group():
                        dpg.add_text(default_value="Input Date")
                        dpg.add_group(tag='search_save_btn', horizontal=True)
                        dpg.add_input_text(tag='date_user',
                                           no_spaces=True,
                                           decimal=True,
                                           width=100,
                                           parent='search_save_btn'
                                           )
                        dpg.add_button(label="Search",
                                       parent='search_save_btn',
                                       callback=lambda x: start_programm(
                                           user_data=dpg.get_value('date_user'),
                                           type_con=dpg.get_value('type_connection')
                                       ))
                        dpg.add_button(label="Save", callback=save_freq, parent='search_save_btn')

                    # Таблица частоты
                    with dpg.table(tag='freq_table'):
                        dpg.add_table_column(label='Team')
                        dpg.add_table_column(label='win_3')
                        dpg.add_table_column(label='win_4')
                        dpg.add_table_column(label='lose')
                        dpg.add_table_column(label='all')
                        dpg.add_table_column(label='percent')

                # Страница настроек 
                with dpg.tab(label='Settings'):
                    with dpg.group():
                        dpg.add_text('Name FreqTable File')
                        dpg.add_input_text(tag='freq_name', default_value=self.data['name_freq_table'])

                    with dpg.group():
                        dpg.add_text('Тип соединения:')
                        dpg.add_combo(
                            items=['selenium', 'playwright'],
                            tag='type_connection',
                            default_value='playwright')

                    dpg.add_button(label='Save Settings',
                                   tag='bth_save_settings',
                                   callback=lambda _: save_settings(dpg.get_value('freq_name')))

            dpg.bind_font("Default font")
            dpg.set_primary_window(window='main_wind', value=True)

            dpg.setup_dearpygui()
            dpg.show_viewport()
            dpg.start_dearpygui()
            dpg.destroy_context()

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
                dpg.add_text(freq_list[team_name_key]['win_3'])
                dpg.add_text(freq_list[team_name_key]['win_4'])
                dpg.add_text(freq_list[team_name_key]['lose'])
                dpg.add_text(freq_list[team_name_key]['all'])
                dpg.add_text(freq_list[team_name_key]['percent'])

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

    def draw_text_in_board(self, message):
        with dpg.group(parent='main', tag='alert_group', horizontal=True):
            dpg.add_text(default_value=message)
            dpg.add_button(
                label='Закрыть',
                callback=lambda x: dpg.delete_item(item='alert_group')
            )
