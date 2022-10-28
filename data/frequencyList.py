class FrequencyList(): 
    def __init__(self) -> None:
        self.freqList = {
            'Тестовая команда': {'pass': 2, 'take': 3, 'total': 5},
        }
        self.freqListWithStructForWriting = []
        self.columns = ['Команда', 'Отдали четверть после половины', 'Забрали четверть после половины', 'Всего']
        
    def __repr__(self) -> str:
        return f'{self.freqList}'

    def getData(self): 
        return self.freqList

    def addTeamInList(self, matchData): 
        for item in [matchData['nameHome'], matchData['nameAway']]: 
            if self.freqList.get(item): 
                if matchData['loser'] == item: 
                    self.freqList[item]['pass'] += 1 
                    self.freqList[item]['total'] = self.freqList[item]['take'] + self.freqList[item]['pass']
                elif matchData['winner'] == item: 
                    self.freqList[item]['take'] += 1 
                    self.freqList[item]['total'] = self.freqList[item]['take'] + self.freqList[item]['pass']
            else: 
                if matchData['loser'] == item: 
                    self.freqList[item] = {
                        'pass': 1, 
                        'take': 0,
                        'total': 1,
                    }
                elif matchData['winner'] == item: 
                    self.freqList[item] = {
                        'pass': 0, 
                        'take': 1,
                        'total': 1,
                    }
    
    def fillDataFrameBeforeSave(self):
        for item in self.freqList:
            self.freqListWithStructForWriting.append([item, self.freqList[item]['pass'], self.freqList[item]['take'], self.freqList[item]['total']])