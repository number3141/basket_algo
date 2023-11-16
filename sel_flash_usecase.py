import json
from use_case.find_statictic import FindStatistic

class SelFlashFindStatistic(FindStatistic):
    def find_statistic_in_data(self) -> None:
        for match in self.data_no_check:
            self.match_list.add_apropriate_match(match)
            self.freq_list.add_match(match)



if __name__ == '__main__': 
    with open('text.txt', 'r', encoding = 'UTF-8') as f:
        dirty_data = json.loads(f.read())
        t = SelFlashFindStatistic(dirty_data)
        t.find_statistic_in_data()
        