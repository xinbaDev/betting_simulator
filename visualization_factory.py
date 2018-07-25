import importlib
from utils import get_class_name
import logging


class VisualizationFactory:

    def __init__(self, settings):
        self.visualization = settings.get('plugin', None)
        self.title = settings.get('title', 'betting')
        self.file = settings.get('file', 'simulation_result\\visualization')


    def create(self):
        try:
            module = importlib.import_module('visualization.{0}'.format(self.visualization))
        except ImportError:
            logging.exception('import error')
        else:
            strategy_module = getattr(module, get_class_name(self.visualization))
            return strategy_module(self.title, self.file)
