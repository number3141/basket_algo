class Match_List():
    def __init__(self) -> None:
        self.match_list = list()

    def get_match_list(self):
        return self.match_list 

    def add_apropriate_match(self, match): 
        self.match_list.append(match)


