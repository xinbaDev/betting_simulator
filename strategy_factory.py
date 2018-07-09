import importlib
from utils import get_class_name

class StrategyFactory:

    def __init__(self, settings):
        self.strategy = settings.get('strategy', None)
        self.initial_money = settings.get('initial_money', 1000)
        self.initial_bet = settings.get('initial_bet', 10)

    def create(self):
        try:
            module = importlib.import_module('strategies.{0}'.format(self.strategy))
        except ImportError:
            return None
        else:
            strategy_module = getattr(module, get_class_name(self.strategy))
            return strategy_module(
                                    initial_money = self.initial_money,
                                    initial_bet = self.initial_bet
                                )
