import os
BASE_DIR = os.path.dirname((os.path.abspath(__file__)))

betting_data_settings = {
    'shuffle': True
}

betting_settings = {
    'strategy': 'regain_all_loss',
    'initial_money': 10000,
    'initial_bet': 100
}

visualization_settings = {
    'plugin': 'multiple_run_visualization',
    'title': 'betting stats',
    'file': BASE_DIR + '/simulation_result/visualization/multiple_run_visualization.html'
}

stimulator_settings = {
    'times': 1000
}

logging_settings = {
    'enable_mutiple_run_logging': True,
    'enable_single_run_logging': False
}
