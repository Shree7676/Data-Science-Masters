from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.io import curdoc


def scatter_plot():
    source = ColumnDataSource(data=dict(x=[1, 2, 3], y=[4, 5, 6]))
    p = figure(title='Scatter Plot', tools=['pan', 'box_zoom', 'reset'])
    p.scatter(x='x', y='y', source=source, size=10)
    return p


curdoc().add_root(scatter_plot())
