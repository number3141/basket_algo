from entity.match import Match

# Адаптер, который настраивает Entity Match 


class MatchBasket(Match): 
    def calc_result(self):
        self.winnerList = []
        for i in [0, 1, 2, 3]: 
            if self.points_home[i] > self.points_away[i]: 
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

    def check_match(self):
        if any([self.result == 'Заход_3', self.result == 'Заход_4', self.result == 'Поражение']):
            return True 
        return False

