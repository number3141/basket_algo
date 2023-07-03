from datetime import datetime

class MatchDate(): 
    """
    Класс, содержащий дату матча 

    Атрибуты: 
    ----------
    date_str : str
        Дата, с какого дня нужно начать "собирать" матчи

    Методы:
    ----------
    decDate()
        Отнимает от текущей даты 1 день
        
    """
    def __init__(self, date_str) -> None:
        self.dateList = date_str.split('.')
        self.day = int(self.dateList[0])
        self.month = int(self.dateList[1])
        self.date = datetime(2022, self.month, self.day)
        

    def __repr__(self) -> str:
        return f'День - {self.day}, Месяц - {self.month}'


    def getDay(self):
        return self.day if self.day >= 10 else f'0{self.day}'  
    

    def getMonth(self): 
        return self.month if self.month >= 10 else f'0{self.month}'


    def decDate(self): 
        """
        Отнимает от текущей даты 1 день
        
        Не принимает аргументов, работает с датой, 
        которую передали при создании экземпляра объекта

        """
        if self.day == 1: 
            if self.month == 1:
                self.day = 31 
                self.month = 12 
            else: 
                self.day = 31
                self.month -= 1
        else: 
            self.day -= 1
