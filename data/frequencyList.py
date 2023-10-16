from data.match import Match


class FrequencyList(): 
    """Лист рассчёта частоты отыгрывания каждой команды"""
    def __init__(self, columns) -> None:
        self.freq_list = dict()
        self.freq_list_with_struct_for_writing = list()
        self.columns = columns
        

    def __repr__(self) -> str:
        return f'{self.freq_list}'


    def get_data(self): 
        return self.freq_list


    def add_team_in_list(self, match: Match): 

        home_team_name = match.get_name_home_team()
        away_team_name = match.get_name_away_team()
        match_result = match.get_result_match()
        match_loser = match.get_match_loser()
        match_winner = match.get_match_winner()

        for item in [home_team_name, away_team_name]: 
            if self.freq_list.get(item): 
                if match_result == 'Поражение':
                    self.freq_list[item]['defeat'] += 1
                    self.freq_list[item]['total'] += 1
                elif match_loser == item: 
                    self.freq_list[item]['pass'] += 1 
                    self.freq_list[item]['total'] += 1
                elif match_winner == item: 
                    self.freq_list[item]['take'] += 1 
                    self.freq_list[item]['total'] += 1
            else: 
                if match_result == 'Поражение':
                    self.freq_list[item] = {
                        'pass': 0, 
                        'take': 0,
                        'defeat': 1,
                        'total': 1,
                    }
                if match_loser == item: 
                    self.freq_list[item] = {
                        'pass': 1, 
                        'take': 0,
                        'defeat': 0,
                        'total': 1,
                    }
                elif match_winner == item: 
                    self.freq_list[item] = {
                        'pass': 0, 
                        'take': 1,
                        'defeat': 0,
                        'total': 1,
                    }
    
    def fill_dataframe_before_save(self):
        for item in self.freq_list:
            self.freq_list_with_struct_for_writing.append([
                item, self.freq_list[item]['pass'], 
                self.freq_list[item]['take'], 
                self.freq_list[item]['defeat'], 
                self.freq_list[item]['total'],
            ])