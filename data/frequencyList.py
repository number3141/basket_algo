class FrequencyList(): 
    def __init__(self) -> None:
        self.freqList = {}
        self.freqListWithStructForWriting = []
        self.sortedTeam = {}
        self.columns = ['Команда', 'Кол-во отыгранных 3ч.']
        
    def __repr__(self) -> str:
        return f'{self.sortedTeam}'

    def getData(self): 
        return self.freqList

    def addTeamInList(self, teamNames): 
        if teamNames: 
            for item in teamNames: 
                if self.freqList.get(item): 
                    self.freqList[item] += 1 
                else: 
                    self.freqList[item] = 1 
            self.sortedKey = sorted(self.freqList, key=self.freqList.get)
            for item in self.sortedKey:
                self.sortedTeam[item] = self.freqList[item]
    
    def fillDataFrameBeforeSave(self):
        for item in self.freqList:
            self.freqListWithStructForWriting.append([item, self.freqList[item]])