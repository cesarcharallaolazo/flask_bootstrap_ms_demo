from flask import render_template
from flask_bootstrap import Bootstrap
from flask import Flask, request

app = Flask(__name__, static_folder='templates/img')
Bootstrap(app)


@app.route('/python', methods=['GET'])
def index_get():
    return render_template('index.html', calc_suma="")


@app.route('/py/eval', methods=['POST'])
def index_post():
    sumando_1 = int(request.values["sumando_1"])
    sumando_2 = int(request.values["sumando_2"])
    return render_template('index.html', calc_suma=str(sumando_1 + sumando_2),
                           sumando1=sumando_1, sumando2=sumando_2)


@app.route('/', methods=['GET'])
def index_root():
    return index_get()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, use_reloader=True)
