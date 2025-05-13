import flask
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')    #отслеживание страницы главной
@app.route('/home')
def index():
    return render_template('commonBase.html')


@app.route('/summary')
def summary():
    return render_template('index— копия.html')


if __name__ == '__main__':
    app.run(debug=True)
