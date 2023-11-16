from entity.match import Match

class Freq_List():
    def __init__(self) -> None:
        self.freq_list = {
            'name_team': {
                'aprop_match': 0, 
                'all_match': 0, 
            } 
        }


    def get_freq_list(self):
        return self.freq_list 


    def add_match(self, match): 
        # Если матч подходит 
        # BAD - Изменения внизу нарушат этот класс. Как переделать?
        for team in [match['name_home'], match['name_away']]: 
            if match['is_inderhand']: 
                if self.freq_list.get(team):
                    self.freq_list[team]['aprop_match'] += 1
                    self.freq_list[team]['all_match'] += 1
                else: 
                    self.freq_list.setdefault(team, {'aprop_match': 1, 'all_match': 1})
            else: 
                # Матч не подошёл по стратегии 
                if self.freq_list.get(team):
                    self.freq_list[team]['aprop_match'] += 0
                    self.freq_list[team]['all_match'] += 1
                else: 
                    self.freq_list.setdefault(team, {'aprop_match': 0, 'all_match': 1})


        

