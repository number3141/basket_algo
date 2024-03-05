from entity.match import Match


# Адаптер, который настраивает Entity Match
class MatchBasket(Match):
    def calc_result(self):
        quarter_winners = list()
        for i in [0, 1, 2, 3]:
            if self.dto_data.points_home[i] > self.dto_data.points_away[i]:
                quarter_winners.append(self.dto_data.name_home)
            else:
                quarter_winners.append(self.dto_data.name_away)

        match quarter_winners:
            case [first, sec, th, _] if first == sec and first != th:
                self.dto_data.loser = quarter_winners[0]
                self.dto_data.winner = quarter_winners[2]
                self.dto_data.win_3 = True
                self.dto_data.result = True
                self.dto_data.underhand = True
            case [first, sec, _, four] if first == sec and first != four:
                self.dto_data.loser = quarter_winners[0]
                self.dto_data.winner = quarter_winners[3]
                self.dto_data.win_4 = True
                self.dto_data.result = True
                self.dto_data.underhand = True
            case [first, sec, _, _] if first == sec:
                self.dto_data.loser = self.dto_data.name_away
                self.dto_data.winner = self.dto_data.name_home
                self.dto_data.result = False
                self.dto_data.underhand = True
            case [first, sec, _, _] if first != sec:
                self.dto_data.underhand = False

        return self.dto_data.underhand
