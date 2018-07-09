# to show the total money change after each bet
from visualization import *

class MoneyHistory(Visualization):

    def generate_graph(self, data):
        layout = go.Layout(title=self.title,
                           xaxis=dict(title='times'),
                           yaxis=dict(title='money'))

        data = [go.Scatter(x = data["x"], y = data["y"])]

        self.fig = go.Figure(data=data, layout=layout)
