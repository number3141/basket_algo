from collections import Counter
from entity.match import MatchDTO


class FreqList:
    def __init__(self) -> None:
        self.freq_list = {
            'name_team': {
                'win_3': 0,
                'win_4': 0,
                'lose': 0,
                'all': 0,
                'percent': 0.0,
            }
        }

        self.win_3_matches = Counter()
        self.win_4_matches = Counter()
        self.lose_mathes = Counter()
        self.all_mathes = Counter()

    def get_freq_list(self):
        for name_team in self.all_mathes:
            self.freq_list.update({
               name_team: {
                   'win_3': self.win_3_matches[name_team],
                   'win_4': self.win_4_matches[name_team],
                   'lose': self.lose_mathes[name_team],
                   'all': self.all_mathes[name_team],
                   'percent': (self.win_4_matches[name_team] + self.win_3_matches[name_team]) / self.all_mathes[name_team]
               }
            })

        return self.freq_list

    def add_match(self, match_dto: MatchDTO):
        if match_dto.get_underhand():
            self.all_mathes.update(Counter({match_dto.get_loser(): 1, match_dto.get_winner(): 1}))

            if match_dto.get_result() and match_dto.get_win_3():
                self.win_3_matches.update(Counter({match_dto.get_loser(): 1, match_dto.get_winner(): 1}))
            elif match_dto.get_result() and match_dto.get_win_4():
                self.win_4_matches.update(Counter({match_dto.get_loser(): 1, match_dto.get_winner(): 1}))
            else:
                self.lose_mathes.update(Counter({match_dto.get_loser(): 1, match_dto.get_winner(): 1}))






