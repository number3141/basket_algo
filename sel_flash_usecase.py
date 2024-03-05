from sel_flash_match import MatchBasket
from use_case.find_statictic import FindStatistic


class SelFlashFindStatistic(FindStatistic):
    def find_statistic_in_data(self) -> None:
        for match_dto in self.data_no_check:
            new_match = MatchBasket()
            new_match.set_dto_data(match_dto)
            new_match.calc_result()
            print(new_match)
            self.freq_list.add_match(new_match.get_dto_data())
