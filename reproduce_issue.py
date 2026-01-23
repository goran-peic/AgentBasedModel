from bokeh.plotting import figure
from bokeh.models import NumeralTickFormatter, Range1d
from bokeh.embed import file_html, components
from bokeh.resources import CDN
import numpy as np

try:
    # Mock data
    x_iter = np.array([1])
    y_grass = np.array([10])
    y_sheep = np.array([5])
    y_wolves = np.array([2])

    tools = "pan,box_zoom,hover,undo,reset,save"

    creature_plot = figure(title="Population Evolution (Counts)", tools=tools, width=700, height=350,
                           toolbar_location="above")
    creature_plot.background_fill_color = "#f4f4f4"
    creature_plot.min_border_left = 20
    creature_plot.background_fill_alpha = 0.68
    creature_plot.xaxis.axis_label = "Iteration"
    creature_plot.yaxis.axis_label = "Count"
    creature_plot.border_fill_color = "black"
    creature_plot.xaxis.axis_label_text_color = \
      creature_plot.yaxis.axis_label_text_color = "white"
    creature_plot.xaxis.major_tick_line_color = creature_plot.xaxis.minor_tick_line_color = \
      creature_plot.yaxis.minor_tick_line_color = creature_plot.yaxis.major_tick_line_color = "white"
    creature_plot.title.text_color = creature_plot.xaxis.major_label_text_color = \
      creature_plot.yaxis.major_label_text_color = "white"
    creature_plot.xaxis.axis_line_color = creature_plot.yaxis.axis_line_color = "white"

    creature_plot.circle(x_iter, y_grass, legend_label="Grass", fill_color="green")
    creature_plot.line(x_iter, y_grass, legend_label="Grass", line_color="green", line_width=2)

    creature_plot.square(x_iter, y_sheep, legend_label="Sheep", fill_color="#ffffff")
    creature_plot.line(x_iter, y_sheep, legend_label="Sheep", line_color="#ffffff", line_width=2)

    creature_plot.triangle(x_iter, y_wolves, legend_label="Wolves", fill_color="red", line_color="red")
    creature_plot.line(x_iter, y_wolves, legend_label="Wolves", line_color="red", line_width=2)

    html_text = file_html(creature_plot, CDN, "Population Evolution")
    script_1, div1 = components(creature_plot)

    print("Plot 1 generated")

    # Plot 2
    # x_range=(1, 0)
    creature_plot2 = figure(x_range=Range1d(1, 0), y_range=Range1d(0, 1), title="Population Evolution (Shares)",
                            tools=tools, width=700, height=350, toolbar_location="above")
    creature_plot2.grid.minor_grid_line_color = '#eeeeee'

    creature_plot2.min_border_left = 20
    creature_plot2.min_border_right = 20
    creature_plot2.xaxis.axis_label = "Iteration"
    creature_plot2.yaxis.axis_label = "Share"
    creature_plot2.border_fill_color = "black"
    creature_plot2.xaxis.axis_label_text_color = \
      creature_plot2.yaxis.axis_label_text_color = "white"
    creature_plot2.xaxis.major_tick_line_color = creature_plot2.xaxis.minor_tick_line_color = \
      creature_plot2.yaxis.minor_tick_line_color = creature_plot2.yaxis.major_tick_line_color = "white"
    creature_plot2.title.text_color = creature_plot2.xaxis.major_label_text_color = \
      creature_plot2.yaxis.major_label_text_color = "white"
    creature_plot2.xaxis.axis_line_color = creature_plot2.yaxis.axis_line_color = "white"

    # Mock areas
    areas = {'Grass Share': np.array([0.5, 0.5]), 'Sheep Share': np.array([0.3, 0.3]), 'Wolf Share': np.array([0.2, 0.2])}
    colors = ['green', 'white', 'red']
    iter2 = np.array([1, 1])

    for a, area in enumerate(areas):
      creature_plot2.patch(iter2, areas[area], color=colors[a], alpha=1, line_color=None)

    creature_plot2.yaxis[0].formatter = NumeralTickFormatter(format="0%")

    html_text2 = file_html(creature_plot2, CDN, "Population Evolution")
    script_2, div2 = components(creature_plot2)

    print("Plot 2 generated")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
