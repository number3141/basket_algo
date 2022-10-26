import re


class Match: 
    def __init__(self, soup):
        self.soup = soup
        self.data = {
            'matchDate' : self.findMatchData(), 
            'nameHome': self.findTeamName('home'), 
            'nameAway': self.findTeamName('away'), 
            'pointHome': self.cutPoint('home'), 
            'pointAway': self.cutPoint('away'),
            'result': ''
        }
  
    def getNameTeam(self): 
        if any([self.data['result'] == 'Заход_3', self.data['result'] == 'Заход_4']):
            return (self.data['nameHome'], self.data['nameAway'])

    def findMatchData(self): 
        """Извлекает дату матча из объекта BS4"""
        data = self.soup.find('div', class_='event__time').text
        return str(data) 

    def findTeamName(self, team):
        """Извлекает имя команды по префиксу *team* """
        # event__participant--home / event__participant--away
        teamName = self.soup.find('div', class_=f'event__participant--{team}').text
        return teamName 

    def cutPoint(self, team): 
        """Возвращает лист очков команды по префиксу"""
        self.points = []
        for part in [1, 2, 3, 4]: 
            self.pointTeamInPart = self.selectPointInPartByPlayField(team, part)
            self.points.append(self.findDecimalNumImStr(self.pointTeamInPart))
        return self.points

    def selectPointInPartByPlayField(self, playField, part):
        return self.soup.select(f'.event__part--{playField}' + f'.event__part--{part}')

    def findDecimalNumImStr(self, findStr):
        # Регулярная строка для поиска всех десятичных чисел 
        self.reg = re.compile('\d{2}')
        # Конверт в строку, потому что тип - ResultSet бьютифушный 
        self.findPointInPart = self.reg.findall(str(findStr))
        return int(*self.findPointInPart)

    def calcResult(self):
        self.winnerList = []
        for i in range(len(self.data['pointHome'])): 
            if self.data['pointHome'][i] > self.data['pointAway'][i]: 
                self.winnerList.append('home')
            else: 
                self.winnerList.append('away')
        
        if self.winnerList[0] == self.winnerList[1]:
            if self.winnerList[0] != self.winnerList[2]:
                self.data['result'] = 'Заход_3'
                return
            elif self.winnerList[0] != self.winnerList[3]:
                self.data['result'] = 'Заход_4'
                return
            else:
                self.data['result'] = 'Поражение'
                return
        else: 
            self.data['result'] = 'Не подходит'
            return

    def getData(self): 
        return self.data

    def __repr__(self) -> str:
        return f"Матч {self.data}"

# if __name__ == '__main__': 
    # frq = FrequencyList()
    # frq.addTeamInList(('Торнадо', 'Питчер'))
    # frq.addTeamInList(['Торнадо', 'Питчер'])
    # frq.addTeamInList(['Торнадо', 'Чикаго'])

    # li = frq.getDatat()
    # print(li)