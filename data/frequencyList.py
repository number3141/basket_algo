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

    def addTeamInList(self, match): 

        home_team_name = match.get_name_home_team()
        away_team_name = match.get_name_home_team()
        match_result = match.get_result_match() 
        match_loser = match.get_match_loser()
        match_winner = match.get_match_winner()

        for item in [home_team_name, away_team_name]: 
            if self.freqList.get(item): 
                if match_result == 'Поражение':
                    self.freqList[item]['defeat'] += 1
                    self.freqList[item]['total'] += 1
                elif match_loser == item: 
                    self.freqList[item]['pass'] += 1 
                    self.freqList[item]['total'] += 1
                elif match_winner == item: 
                    self.freqList[item]['take'] += 1 
                    self.freqList[item]['total'] += 1
            else: 
                if match_result == 'Поражение':
                    self.freqList[item] = {
                        'pass': 0, 
                        'take': 0,
                        'defeat': 1,
                        'total': 1,
                    }
                if match_loser == item: 
                    self.freqList[item] = {
                        'pass': 1, 
                        'take': 0,
                        'defeat': 0,
                        'total': 1,
                    }
                elif match_winner == item: 
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