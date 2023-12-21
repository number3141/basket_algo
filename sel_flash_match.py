from entity.match import Match


# Адаптер, который настраивает Entity Match
class MatchBasket(Match):
    def calc_result(self):
        quarter_winners = list()
        for i in [0, 1, 2, 3]:
            if self.data.points_home[i] > self.data.points_away[i]:
                quarter_winners.append(self.data.name_home)
            else:
                quarter_winners.append(self.data.name_away)

        if quarter_winners[0] == quarter_winners[1]:
            print('Подходит!')
            self.data.underhand = True
            if quarter_winners[0] != quarter_winners[2]:
                self.data.set_loser(quarter_winners[0])
                self.data.set_winner(quarter_winners[2])
                self.data.win_3 = True
                self.data.result = True
            elif quarter_winners[0] != quarter_winners[3]:
                self.data.loser = quarter_winners[0]
                self.data.winner = quarter_winners[3]
                self.data.win_4 = True
                self.data.result = True
            else:
                self.data.loser = self.data.name_away
                self.data.winner = self.data.name_home
                self.data.result = False
        else:
            # Матч не подошёл 
            self.data.underhand = False

        return self.data.underhand
