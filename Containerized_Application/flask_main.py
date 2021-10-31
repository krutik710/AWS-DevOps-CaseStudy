from flask import Flask
from flask import request, render_template

app = Flask(__name__)


@app.route('/')
def dummy_landing():
    """
    Dummy Landing to take input
    :return: index.html
    """
    return render_template('index.html')


@app.route('/factorial', methods=['POST'])
def factorial():
    """
    Calculates factorial of number
    :return: factorial of number
    """
    if request.method == 'POST':
        n = int(request.form['number'])
        res = 1
        for i in range(2, n+1):
            res *= i
        return str(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
