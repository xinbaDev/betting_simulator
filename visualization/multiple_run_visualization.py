# to show the total money change after each bet
from visualization import *

class MultipleRunVisualization(Visualization):

    def generate_graph(self, data):
        layout = go.Layout(title=self.title,
                           xaxis=dict(title='money'),
                           yaxis=dict(title='times'))

        data = [go.Histogram(x=data)]

        self.fig = go.Figure(data=data, layout=layout)
