import re


class Match: 
    def __init__(self, soup):
        self.soup = soup
        self.match_date = self.find_match_data()
        self.name_home = self.find_team_name_home()
        self.name_away = self.find_team_name_away()
        self.point_home = self.cut_point_home()
        self.point_away = self.cut_point_away()
        self.loser = ''
        self.winner = ''
        self.result = ''

    
    def find_match_data(self):
        raise NotImplementedError(
            f"Определите find_match_data в {self.__class__.__name__}"
        )
    

    def find_team_name_home(self):
        raise NotImplementedError(
            f"Определите find_team_name_home в {self.__class__.__name__}"
        )
    

    def find_team_name_away(self):
        raise NotImplementedError(
            f"Определите find_team_name_away в {self.__class__.__name__}"
        )
    

    def cut_point_home(self):
        raise NotImplementedError(
            f"Определите cut_point_home в {self.__class__.__name__}"
        )
    

    def cut_point_away(self):
        raise NotImplementedError(
            f"Определите cut_point_away в {self.__class__.__name__}"
        )


    def get_result_match(self):
        return self.result


    def get_match_loser(self):
        return self.loser
    

    def get_match_winner(self):
        return self.winner


    def get_match_date(self): 
        return self.match_date
    

    def get_name_home_team(self):
        return self.name_home


    def get_name_away_team(self): 
        return self.name_away


    def get_points_home(self): 
        return self.point_home


    def get_points_away(self): 
        return self.point_away


    def __repr__(self) -> str:
        return f"Матч {self.name_home} and {self.name_away}"


class MatchBasket(Match): 
    def __init__(self, soup):
        super().__init__(soup)

    def isAppropriateMatch(self):
        if any([self.result == 'Заход_3', self.result == 'Заход_4', self.result == 'Поражение']):
            return True 
        return False
        

    def find_match_data(self): 
        """Извлекает дату матча из объекта BS4"""
        data = self.soup.find('div', class_='event__time').text
        return str(data) 


    def find_team_name_home(self):
        return self.soup.find('div', class_=f'event__participant--home').text
    

    def find_team_name_away(self):
        return self.soup.find('div', class_=f'event__participant--away').text


    def cut_point_home(self): 
        """Возвращает лист очков домашней команды"""
        self.points = []
        for part in [1, 2, 3, 4]: 
            # self.pointTeamInPart = self.selectPointInPartByPlayField(team, part)
            self.pointTeamInPart = self.soup.select(f'.event__part--home' + f'.event__part--{part}')
            self.points.append(self.findDecimalNumImStr(self.pointTeamInPart))
        return self.points
    

    def cut_point_away(self): 
        """Возвращает лист очков гостевой команды"""
        self.points = []
        for part in [1, 2, 3, 4]: 
            # self.pointTeamInPart = self.selectPointInPartByPlayField(team, part)
            self.pointTeamInPart = self.soup.select(f'.event__part--away' + f'.event__part--{part}')
            self.points.append(self.findDecimalNumImStr(self.pointTeamInPart))
        return self.points


    def findDecimalNumImStr(self, findStr):
        # Регулярная строка для поиска всех десятичных чисел 
        self.reg = re.compile('\d{2}')
        # Конверт в строку, потому что тип - ResultSet бьютифушный 
        self.findPointInPart = self.reg.findall(str(findStr))
        return int(*self.findPointInPart)


    def calcResult(self):
        self.winnerList = []
        for i in [0, 1, 2, 3]: 
            if self.point_home[i] > self.point_away[i]: 
                self.winnerList.append(self.name_home)
            else: 
                self.winnerList.append(self.name_away)
        
        if self.winnerList[0] == self.winnerList[1]:
            self.loser = self.winnerList[0]
            if self.winnerList[0] != self.winnerList[2]:
                self.winner = self.winnerList[2]
                self.result = 'Заход_3'
                return
            elif self.winnerList[0] != self.winnerList[3]:
                self.winner = self.winnerList[3]
                self.result = 'Заход_4'
                return
            else:
                self.result = 'Поражение'
                return
        else: 
            self.result = 'Не подходит'
            return