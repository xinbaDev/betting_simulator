import os
BASE_DIR = os.path.dirname((os.path.abspath(__file__)))

betting_data_settings = {
    'shuffle': True
}

betting_settings = {
    'strategy': 'double_betting_after_winning',
    'initial_money': 10000,
    'initial_bet': 100
}

visualization_settings = {
    'plugin': 'money_history',
    'title': 'betting history',
    'file': BASE_DIR + '/simulation_result/visualization/double_betting_after_winning.html'
}

