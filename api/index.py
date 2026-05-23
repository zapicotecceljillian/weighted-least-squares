from flask import Flask, render_template, request
from methods.wls import weighted_least_squares

app = Flask(__name__,
template_folder='../templates',
static_folder='../static')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/examples')
def examples():
    return render_template('examples.html')


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():

    result = None
    error = None

    if request.method == 'POST':

        try:

            x = list(map(float,
            request.form['x'].split(',')))

            y = list(map(float,
            request.form['y'].split(',')))

            w = list(map(float,
            request.form['w'].split(',')))

            result = weighted_least_squares(x, y, w)

        except Exception as e:

            error = str(e)

    return render_template(
        'calculator.html',
        result=result,
        error=error
    )


if __name__ == '__main__':
    app.run(debug=True)