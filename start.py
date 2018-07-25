from betting_simulator import Simulator
from config import stimulator_settings, visualization_settings
from visualization_factory import VisualizationFactory

if __name__ == '__main__':
    stimulator = Simulator()

    stats = []
    times = stimulator_settings.get('times', 100)
    for i in range(times):
        stimulator.setup(enable_visualization=False)
        result = stimulator.run()
        stats.append(result[-1])

    money = []
    for stat in stats:
        money.append(stat['current_money'])

    visualization = VisualizationFactory(visualization_settings).create()
    visualization.generate_graph(money)
    visualization.save()
