import json
from entity.match import Match
from sel_flash_match import MatchBasket
from use_case.find_statictic import FindStatistic


class SelFlashFindStatistic(FindStatistic):
    def find_statistic_in_data(self) -> None:
        for match_dto in self.data_no_check:
            print(match_dto)
            new_match = MatchBasket()
            new_match.set_data(match_dto)
            new_match.calc_result()
            self.match_list.add_apropriate_match(new_match.get_data())
            self.freq_list.add_match(new_match.get_data())


if __name__ == '__main__': 
    with open('text.txt', 'r', encoding = 'UTF-8') as f:
        dirty_data = json.loads(f.read())
        t = SelFlashFindStatistic(dirty_data)
        t.find_statistic_in_data()
        