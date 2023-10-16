import abc 

from bs4 import BeautifulSoup 

from parse_web.matchDate import MatchDate


class Interface_Soup_From_HTML(): 
    """
    Интерфейс для классов, перебирающих контент сайта в суп
    """
    def create_soup_from_flashscore(self, date_string, content):
        return Soup_From_HTML_FlashScore(date_string, content).get_all_found_matches()


class Soup_From_HTML(abc.ABC): 
    """
    Класс, перебирающий контент сайта в "суп" 

    Атрибуты:
    ----------
    soup - html-разметка сайта 
     
    """
    @abc.abstractmethod
    def get_all_found_matches(self):
        "Возвращение всех найденных матчей"


class Soup_From_HTML_FlashScore(Soup_From_HTML):
    """
    Класс, перебирающий контент сайта в "суп" с сайта Flashscore  

    Атрибуты:
    ----------
    dateString:
    """
    def __init__(self, dateString, content) -> None:
        self.date = MatchDate(dateString)
        self.soup = BeautifulSoup(content, 'lxml')
  

    def __repr__(self) -> str:
        return f'Объект - {self.soup}'


    def get_all_found_matches(self):
        """Пока не найдёт ближайшие матчи - будет уменьшать дату"""
        while True: 
            self.stopMatch = self.find_stop_match()
            if self.stopMatch: 
                # Склеенный массив 
                self.findMatch = [self.stopMatch] + list(self.stopMatch.find_all_previous('div', class_ = 'event__match'))
                return self.findMatch
    
    
    def find_stop_match(self):
        """Получает дату и находит последний матч, перебирая все времена, в которых играют команды"""
        self.timeList = ['01:00', '01:30', '02:30', '02:30', '03:00', '03:30', '04:00', '04:30', '05:00',
        '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30']
        
        while True: 
            for time in self.timeList:
                print(f"{self.date.getDay()}.{self.date.getMonth()} {time}")
                self.stopMatch = self.isMatchWithDate(time)
                if self.stopMatch: 
                    return self.stopMatch
            self.date.decDate()
    

    def isMatchWithDate(self, time): 
        try: 
            stringForFind = f"{self.date.getDay()}.{self.date.getMonth()}. {time}"
            # parent из-за того, что возвращается строка, а нам нужен весь матч (родитель)
            findMatch = self.soup.find(string=stringForFind).parent.parent
            return findMatch
        except: 
            return False
