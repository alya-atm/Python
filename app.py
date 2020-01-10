from flask import Flask, render_template, request
from data import df
from models.outliers import outliers
from models.plot1 import make_plot
from models.xgboost import model_xgb
from models.lgb import model_lgb
from models.random_forest import model_rf
from models.plot_model import make_plot_model, part_plot_model
from models.metrics import MAPE, WAPE, RMSE, BIAS
from sklearn.metrics import mean_absolute_error
import pandas as pd
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def show():
    global ex, pl2
    error = None
    error_sku = None
    save=None
    store = df['store'].unique()
    sku = df['sku'].unique()
    tk = request.args.get('store')
    item = request.args.get('sku')
    if tk is None and item is None:
        tk = 370
        item = 3041866
        ex = df[(df['store'] == tk) & (df['sku'] == item)].reset_index(drop=True)
    elif len(item) == 0:
        error_sku = 'Выберите товар'
    elif int(tk) in store and int(item) in sku:
        if len(df[(df['store'] == int(tk)) & (df['sku'] == int(item))].reset_index(drop=True)) == 0:
            error = 'Товар не продается в магазине'
        else:
            ex = df[(df['store'] == int(tk)) & (df['sku'] == int(item))].reset_index(drop=True)
    clear = outliers(ex)
    plots1 = []
    plots1.append(make_plot(clear))
    model = request.args.get('model')
    if model is None:
        model = 'Xgboost'
        pl2 = model_xgb(clear)
    if model == 'Xgboost':
        pl2 = model_xgb(clear)
    elif model == 'Lightgbm':
        pl2 = model_lgb(clear)
    elif model == 'Random forest':
        pl2 = model_rf(clear)
    plots2 = []
    plots2.append(make_plot_model(pl2))
    plots3 = []
    plots3.append(part_plot_model(pl2))
    model_test = pl2[1]
    y_test = pl2[2]
    wape = round(WAPE(y_test, model_test), 2)
    mape = round(MAPE(y_test, model_test), 2)
    bias = round(BIAS(y_test, model_test), 2)
    rmse = round(RMSE(y_test, model_test), 2)
    mae = round(mean_absolute_error(y_test, model_test), 2)

    if request.method == 'POST':
        data_models = pd.read_csv('models.csv')
        if len(data_models[(data_models['store'] == int(tk)) & (data_models['sku'] == int(item))]) != 0:
            save = data_models[(data_models['store'] == int(tk)) & (data_models['sku'] == int(item))]['model']
            save = save.values[0]
        else:
            values = [tk, item, model]
            with open('models.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(values)

    return render_template('base.html', plots1=plots1, plots2=plots2, plots3=plots3, wape=wape, mape=mape, rmse=rmse,
                           bias=bias, mae=mae, model=model, store=store, tk=tk, sku=sku, item=item, error=error,
                           error_sku=error_sku,save=save)

if __name__ == '__main__':
    app.run()
