import plotly.graph_objs as go
import plotly.offline as offline

class Visualization:

    def __init__(self, title, file):
        self.title = title
        self.file = file

    def generate_graph(self):
        pass

    def save(self):
        offline.plot(self.fig, image='png', filename=self.file)
