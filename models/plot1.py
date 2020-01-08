from bokeh.plotting import figure
from bokeh.embed import components
import pandas as pd
def make_plot(clear):
    ex=clear[0]
    outliers_index=clear[1]
    a = ex.loc[outliers_index, ['date', 'sales_m']]
    TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select,hover"
    p = figure(plot_width=900, plot_height=390,  x_axis_type="datetime",
               y_axis_label="Продажи, шт",
               x_axis_label="Дата",
               tools=TOOLS)
    p.circle(a['date'], a['sales_m'], color='#079F7F', line_width=4, legend_label="Выбросы")
    p.line(ex['date'], ex['sales_m'], color='black', line_width=2, line_dash=(2, 2), legend_label="Средние продажи")
    p.line(ex['date'], ex['sales_without_outliers'], color='#A2004E', line_width=2,
           legend_label="Средние продажи без выбросов")

    #p.background_fill_color = "#2F2F2F"
    #p.border_fill_color = '#2F2F2F'
    p.outline_line_color = '#444444'
    #p.axis.axis_line_color = "white"
    #p.axis.axis_label_text_color = "white"
    #p.axis.major_label_text_color = "white"

    p.legend.background_fill_color = "white"
    #p.legend.label_text_color = "white"
    p.grid.grid_line_alpha = 1
    script, div = components(p)
    return script, div
