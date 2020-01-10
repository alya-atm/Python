from bokeh.plotting import figure
from bokeh.embed import components

def make_plot_model(xgb_data):
    ex, XB_test, y_test=xgb_data
    TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select,hover"
    p = figure(plot_width=900, plot_height=390, x_axis_type="datetime",
               y_axis_label="Продажи, шт",
               x_axis_label="Дата",
               tools=TOOLS)
    test_size = 12
    p.line(ex['date'], ex['sales_without_outliers'], color='#A2004E', line_width=2, legend_label="Фактические данные")
    p.line(ex[-test_size:]['date'], XB_test, color='#079F7F', line_width=2, legend_label="Прогноз")
    p.outline_line_color = '#444444'
    p.grid.grid_line_alpha = 1
    script, div = components(p)
    return script, div

def part_plot_model(xgb_data):
    ex, model_test, y_test = xgb_data
    test_size = 12
    TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select,hover"

    p = figure(plot_width=900, plot_height=390, x_axis_type="datetime",
               y_axis_label="Продажи, шт",
               x_axis_label="Дата",
               tools=TOOLS)
    p.line(ex[-test_size:]['date'], y_test, color='#A2004E', line_width=2, legend_label="Фактические данные")
    p.line(ex[-test_size:]['date'], model_test, color='#079F7F', line_width=2, legend_label="Прогноз")
    p.outline_line_color = '#444444'
    p.grid.grid_line_alpha = 1
    script, div = components(p)
    return script, div