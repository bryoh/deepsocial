from flask import Flask, render_template
from views.chart_examples import create_chart_elements
# from chart_examples import create_chart_elements
from pprint import pprint


app = Flask(__name__)


@app.route('/')
def index():
    ret = create_chart_elements('test', ["#E24736", "#FF9438", "#FFF249"], [5, 5.5, 10], "PolarArea")

    div = ret['canvas'] 
    script= ret['body_script']
    dom_manipulation_script=ret['dom_script']
    pprint(div)
    pprint(script)
    pprint(dom_manipulation_script)
    return render_template('index_.html', 
                           div=div, 
                           script=script,
                          dom= dom_manipulation_script)


if __name__ == '__main__':
    app.run()
