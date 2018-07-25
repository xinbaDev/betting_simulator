from .strategy import Strategy
from utils import configure_logger
from config import logging_settings


class RegainAllLoss(Strategy):

    def exceute(self):
        current_bet = self.initial_bet
        current_money = self.initial_money
        max_money = current_money
        betting_history = []
        for index, odd in enumerate(self.odds):

            if not self._betting_condition(self.odds_ratio[index]):
                continue

            current_money = self._bet(current_money, current_bet)
            if current_money <= 0:
                return betting_history

            if self.result[index] == 'win':
                current_money += (current_bet * float(odd))
                if current_money > max_money:
                    max_money = current_money
                current_bet = self._cal_bet_after_winning(current_money)
            else:
                current_bet = self._cal_bet_after_lossing(current_money, max_money, self.odds[index+1])

            if logging_settings.get('enable_single_run_logging', False):
                logger = configure_logger("betting", "RegainAllLoss.csv")
                logger.info("Index:{}, current_money:{}, current_bet:{}, max_money: {}, odd: {}".format(index, current_money, current_bet, max_money, self.odds[index+1]))

            betting_history.append({'index':index, 'current_money':current_money, 'current_bet':current_bet, 'max_money': max_money})

        return betting_history

    # betting according to odd_ratio(odd_home/odd_away)
    def _betting_condition(self, odd_ratio):
        return 0.5 < float(odd_ratio) and float(odd_ratio) < 1

    def _bet(self, current_money, current_bet):
        current_money -= current_bet
        return current_money

    def _cal_bet_after_winning(self, current_money):
        current_bet = self.initial_bet
        return current_bet

    # if loss, next bet try to recover from the loss
    def _cal_bet_after_lossing(self, current_money, max_money, odd):
        if float(odd) == 1:
            return max_money - current_money
        return (max_money - current_money) / (float(odd) - 1)
