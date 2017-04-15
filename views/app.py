from flask import Flask, render_template
import chartjs

app = Flask(__name__)


@app.route('/')
def index():
    div, script = chart_example()
    return render_template('index_.html', 
                           div=div, 
                           script=script)


def chart_example():
    # Make a pie chart
    mychart = chartjs.chart("Sample pie chart", "PolarArea")
    # Add labels, colors, highlights and data values
    mychart.set_labels(["Apple", "Orange", "Banana"])
    mychart.set_colors(["#E24736", "#FF9438", "#FFF249"])
    mychart.set_highlights(["#E07369", "#FFAC68", "#FFF293"])
    mychart.add_dataset([5,2.3,10])
    print(mychart.make_chart())
    return mychart.make_chart_canvas(), mychart.make_chart_onload()

if __name__ == '__main__':
    app.run()
