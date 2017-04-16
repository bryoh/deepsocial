from flask import Flask, render_template
from chart_examples import chart_example 

app = Flask(__name__)


@app.route('/')
def index():
    div, script = chart_example()
    return render_template('index_.html', 
                           div=div, 
                           script=script)


if __name__ == '__main__':
    app.run()
