from entity.match import Match

# Адаптер, который настраивает Entity Match 

class MatchBasket(Match):               
    def calc_result(self):
        self.winnerList = list()
        for i in [0, 1, 2, 3]: 
            if self.data.points_home[i] > self.data.points_away[i]: 
                self.winnerList.append(self.data.name_home)
            else: 
                self.winnerList.append(self.data.name_away)

        if self.winnerList[0] == self.winnerList[1]:
            print('Подходит!')
            self.data.underhand = True
            if self.winnerList[0] != self.winnerList[2]:
                self.data.set_loser(self.winnerList[0])
                self.data.set_winner(self.winnerList[2])
                self.data.win_3 = True
                self.data.result = True 
            elif self.winnerList[0] != self.winnerList[3]:
                self.data.loser = self.winnerList[0]
                self.data.winner = self.winnerList[3]
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

