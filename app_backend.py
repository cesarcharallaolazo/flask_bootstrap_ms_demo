from flask import Flask, request

app = Flask(__name__)


@app.route('/py/eval', methods=['POST'])
def index_post():
    sumando_1 = int(request.values["sumando_1"])
    sumando_2 = int(request.values["sumando_2"])
    return str(sumando_1 + sumando_2)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, use_reloader=True)
