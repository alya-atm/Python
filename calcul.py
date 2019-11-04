from flask import Flask, render_template, request

calcul = Flask(__name__)
calcul.route("/test",)

def test():
    values = request.form.get('values')


if __name__ == '__main__':
    calcul.run()