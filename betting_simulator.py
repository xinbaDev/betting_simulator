from strategy_factory import StrategyFactory
from visualization_factory import VisualizationFactory
from config import betting_settings, visualization_settings, betting_data_settings
from exception import StrategyNotFoundException
import logging
from random import shuffle

class Simulator:

    def __init__(self):
        self.betting_strategy = None

    def setup(self, enable_visualization):
        if enable_visualization:
            self.visualization = VisualizationFactory(visualization_settings).create()
        else:
            self.visualization = None

        self.betting_strategy = StrategyFactory(betting_settings).create()
        if self.betting_strategy is None:
            raise StrategyNotFoundException('strategy not found, make sure strategy class exist')
        else:
            self._load_data(betting_data_settings)

    def run(self):
        try:
            results = self.betting_strategy.exceute()
        except:
            logging.exception("failed to exceute stimulator")
        else:
            if self.visualization:
                self.visualization.generate_graph({'x':list(range(len(results))), 'y':[result['current_money'] for result in results]})
                self.visualization.save()

            return results

    def _load_data(self, betting_data_settings):
        results = []
        odds_ratios = []
        odds = []
        with open('betting data/processed result/processed_result.csv','r') as fr:
            lines = [line for line in fr]

        if betting_data_settings.get('shuffle', None):
            shuffle(lines)

        for line in lines:
            result, odds_ratio, odd_home, odd_away = line.split(",")
            results.append(result)
            odds_ratios.append(odds_ratio)
            odds.append(odd_home)

        self.betting_strategy.result = results
        self.betting_strategy.odds_ratio = odds_ratios
        self.betting_strategy.odds = odds
