from .strategy import Strategy
from utils import configure_logger
from config import logging_settings


class DoubleBettingAfterWinning(Strategy):

    max_double_betting_times = 3
    double_betting_times = 0

    def exceute(self):
        current_bet = self.initial_bet
        current_money = self.initial_money
        betting_history = []
        for index, odd in enumerate(self.odds):
            if not self._betting_condition(self.odds_ratio[index]):
                continue

            current_money = self._bet(current_money, current_bet)
            if current_money <= 0:
                return betting_history

            if self.result[index] == 'win':
                current_money += (current_bet * float(odd))
                current_bet = self._cal_bet_after_winning(current_bet)
            else:
                current_bet = self._cal_bet_after_lossing()

            if logging_settings.get('enable_single_run_logging', False):
                logger = configure_logger("betting", "DoubleBettingAfterWinning.csv")
                logger.info("Index:{}, current_money:{}, current_bet:{}, odds:{}".format(index, current_money,current_bet, odd))

            betting_history.append({'index':index, 'current_money':current_money, 'current_bet':current_bet})

        return betting_history

    # betting according to odd_ratio(odd_home/odd_away)
    def _betting_condition(self, odd_ratio):
        return 0.5 < float(odd_ratio) and float(odd_ratio) < 1

    def _bet(self, current_money, current_bet):
        current_money -= current_bet
        return current_money

    def _cal_bet_after_winning(self, current_bet):
        if self.double_betting_times < self.max_double_betting_times:
            self.double_betting_times += 1
            return current_bet * 2
        else:
            self.double_betting_times = 0
            return self.initial_bet

    def _cal_bet_after_lossing(self):
        self.double_betting_times = self.max_double_betting_times
        return self.initial_bet
