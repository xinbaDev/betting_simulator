from abc import (
    ABCMeta,
    abstractmethod
)

class Strategy(metaclass=ABCMeta):

    # game result
    # ['win','loss'...]
    result = []

    # odds for home and away
    # [{"odd_home":1, "odd_away":2}...]
    odds = []

    # odd_home/odd_away
    odds_ratio = []

    def __init__(self, initial_money = 10000, initial_bet = 10):
        self.initial_money = initial_money
        self.initial_bet = initial_bet

    @abstractmethod
    def exceute(self):
        raise NotImplementedError("Strategy classes must implement this method")

    @abstractmethod
    def _betting_condition(self):
        raise NotImplementedError("Strategy classes must implement this method")

    @abstractmethod
    def _bet(self, current_money, current_bet):
        raise NotImplementedError("Strategy classes must implement this method")

    @abstractmethod
    def _cal_bet_after_winning(self):
        raise NotImplementedError("Strategy classes must implement this method")

    @abstractmethod
    def _cal_bet_after_lossing(self):
        raise NotImplementedError("Strategy classes must implement this method")
