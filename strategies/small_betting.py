from .strategy import Strategy
import logging

class SmallBetting(Strategy):

    def exceute(self):
        current_bet = self.initial_bet
        current_money = self.initial_money
        for index, odd in enumerate(self.odds):
            if not self._betting_condition(self.odds_ratio[index]):
                continue

            current_money = self._bet(current_money, current_bet)
            if current_money <= 0:
                return [index, 0]

            if self.result[index] == 'win':
                current_money += (current_bet * float(odd))
                current_bet = self._cal_bet_after_winning()
            else:
                current_bet = self._cal_bet_after_lossing(current_bet)

            logging.info("Index:{}, current_money:{}, current_bet:{}".format(index, current_money,current_bet))

        return [index, current_money]

    # betting according to odd_ratio(odd_home/odd_away)
    def _betting_condition(self, odd_ratio):
        return 0.5 < float(odd_ratio) and float(odd_ratio) < 1

    def _bet(self, current_money, current_bet):
        current_money -= current_bet
        return current_money

    def _cal_bet_after_winning(self):
        current_bet = self.initial_bet
        return current_bet

    def _cal_bet_after_lossing(self, current_bet):
        return current_bet
