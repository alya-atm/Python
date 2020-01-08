from flask import Flask, render_template, request
from data import STORE, df
from models.outliers import outliers
from models.plot1 import make_plot
from models.xgboost import model_xgb
from models.lgb import model_lgb
from models.random_forest import model_rf
from models.plot_model import make_plot_model, part_plot_model
from models.metrics import MAPE, WAPE, RMSE, BIAS
from sklearn.metrics import mean_absolute_error

app = Flask(__name__)


@app.route('/', methods=['GET'])
def show():
    store = STORE

    tk = request.args.get('store')
    if tk is None:
        tk=456
        ex = df[(df['store'] == int(tk)) & (df['sku'] == 3022321)].reset_index(drop=True)
    elif int(tk) in store:
        ex = df[(df['store'] == int(tk)) & (df['sku'] == 3022321)].reset_index(drop=True)
    clear = outliers(ex)
    plots1 = []
    plots1.append(make_plot(clear))

    model = request.args.get('model')
    if model is None:
        model = 'xgboost'
        pl2 = model_xgb(clear)
    if model == 'xgboost':
        pl2 = model_xgb(clear)
    elif model == 'lightgbm':
        pl2 = model_lgb(clear)
    elif model == 'random forest':
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

    return render_template('base.html', plots1=plots1, plots2=plots2, plots3=plots3, wape=wape, mape=mape, rmse=rmse,
                           bias=bias, mae=mae, model=model, store=store)


if __name__ == '__main__':
    app.run()
