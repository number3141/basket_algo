import re


class Match: 
    def __init__(self, soup):
        self.soup = soup
        self.match_date = self.findMatchData()
        self.name_home = self.findTeamNameHome()
        self.name_away = self.findTeamNameAway()
        self.point_home = self.cutPointHome()
        self.point_away = self.cutPointAway()
        self.loser = ''
        self.winner = ''
        self.result = ''

    
    def findMatchData(self):
        raise NotImplementedError(
            f"Определите findMatchData в {self.__class__.__name__}"
        )
    

    def findTeamNameHome(self):
        raise NotImplementedError(
            f"Определите findTeamNameHome в {self.__class__.__name__}"
        )
    

    def findTeamNameAway(self):
        raise NotImplementedError(
            f"Определите findTeamNameAway в {self.__class__.__name__}"
        )
    

    def cutPointHome(self):
        raise NotImplementedError(
            f"Определите cutPointHome в {self.__class__.__name__}"
        )
    

    def cutPointAway(self):
        raise NotImplementedError(
            f"Определите cutPointAway в {self.__class__.__name__}"
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
        

    def findMatchData(self): 
        """Извлекает дату матча из объекта BS4"""
        data = self.soup.find('div', class_='event__time').text
        return str(data) 


    def findTeamNameHome(self):
        return self.soup.find('div', class_=f'event__participant--home').text
    

    def findTeamNameAway(self):
        return self.soup.find('div', class_=f'event__participant--away').text


    def cutPointHome(self): 
        """Возвращает лист очков домашней команды"""
        self.points = []
        for part in [1, 2, 3, 4]: 
            # self.pointTeamInPart = self.selectPointInPartByPlayField(team, part)
            self.pointTeamInPart = self.soup.select(f'.event__part--home' + f'.event__part--{part}')
            self.points.append(self.findDecimalNumImStr(self.pointTeamInPart))
        return self.points
    

    def cutPointAway(self): 
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

    
    
