class FrequencyList(): 
    """Лист рассчёта частоты отыгрывания каждой команды"""
    def __init__(self) -> None:
        self.freqList = {
            'Тестовая команда': {
                'pass': 2, 
                'take': 3, 
                'defeat': 0, 
                'total': 5, 
                },
        }
        self.freqListWithStructForWriting = []
        self.columns = [
            'Команда', 
            'Отдали четверть после половины', 
            'Забрали четверть после половины', 
            'Проиграли по страте', 
            'Всего', 
            ]
        
    def __repr__(self) -> str:
        return f'{self.freqList}'

    def getData(self): 
        return self.freqList

    def addTeamInList(self, matchData): 
        for item in [matchData['nameHome'], matchData['nameAway']]: 
            if self.freqList.get(item): 
                if matchData['result'] == 'Поражение':
                    self.freqList[item]['defeat'] += 1
                    self.freqList[item]['total'] += 1
                elif matchData['loser'] == item: 
                    self.freqList[item]['pass'] += 1 
                    self.freqList[item]['total'] += 1
                elif matchData['winner'] == item: 
                    self.freqList[item]['take'] += 1 
                    self.freqList[item]['total'] += 1
            else: 
                if matchData['result'] == 'Поражение':
                    self.freqList[item] = {
                        'pass': 0, 
                        'take': 0,
                        'defeat': 1,
                        'total': 1,
                    }
                if matchData['loser'] == item: 
                    self.freqList[item] = {
                        'pass': 1, 
                        'take': 0,
                        'defeat': 0,
                        'total': 1,
                    }
                elif matchData['winner'] == item: 
                    self.freqList[item] = {
                        'pass': 0, 
                        'take': 1,
                        'defeat': 0,
                        'total': 1,
                    }
    
    def fillDataFrameBeforeSave(self):
        for item in self.freqList:
            self.freqListWithStructForWriting.append([
                item, self.freqList[item]['pass'], 
                self.freqList[item]['take'], 
                self.freqList[item]['defeat'], 
                self.freqList[item]['total'],
            ])