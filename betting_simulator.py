from strategy_factory import StrategyFactory
from visualization_factory import VisualizationFactory
from config import betting_settings, visualization_setting
from exception import StrategyNotFoundException
import logging


class Simulator:

    def __init__(self):
        self.betting_strategy = None
        self.visualization_setting = None

    def setup(self):
        self.visualization = VisualizationFactory(visualization_setting).create()
        self.betting_strategy = StrategyFactory(betting_settings).create()
        if self.betting_strategy is None:
            raise StrategyNotFoundException('strategy not found, make sure strategy class exist')
        else:
            self._load_data()

    def run(self):
        try:
            results = self.betting_strategy.exceute()
        except:
            logging.exception("failed to exceute stimulator")
        else:
            if self.visualization:
                self.visualization.generate_graph({'x':list(range(len(results))), 'y':[result['current_money'] for result in results]})
                self.visualization.save()

    def _load_data(self):
        results = []
        odds_ratios = []
        odds = []
        with open('betting data/processed result/processed_result.csv','r') as fr:
            for line in fr:
                result, odds_ratio, odd_home, odd_away = line.split(",")
                results.append(result)
                odds_ratios.append(odds_ratio)
                odds.append(odd_home)

        # results.reverse()
        # odds_ratios.reverse()
        # odds.reverse()
        self.betting_strategy.result = results
        self.betting_strategy.odds_ratio = odds_ratios
        self.betting_strategy.odds = odds
