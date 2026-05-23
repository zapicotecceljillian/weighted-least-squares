import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
        )
    )
)

from flask import Flask, render_template, request

from methods.wls import weighted_least_squares

app = Flask(
    __name__,
    template_folder='../templates',
    static_folder='../static'
)

@app.route('/')
def home():
    return render_template('index.html')

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

            if len(x) != len(y) or len(y) != len(w):

                error = "All inputs must have equal lengths."

            else:

                result = weighted_least_squares(x, y, w)

        except:

            error = "Invalid Input"

    return render_template(
        'calculator.html',
        result=result,
        error=error
    )

@app.route('/examples')
def examples():
    return render_template('examples.html')

if __name__ == "__main__":
    app.run(debug=True)