from flask import Flask, render_template
from views.chart_examples import create_chart_elements
from datacollection import instagram
# from chart_examples import create_chart_elements
from pprint import pprint


app = Flask(__name__)


def return_ordered_div_elements(dictionary):
    """
    :param dictionary:
    :return: div, script, dom_manipulation script

    returns a list of div, script(with variables), script for dom-manipulation
    """
    div = dictionary['canvas']
    script = dictionary['body_script']# .get_text()  # remove the tags
    dom_manipulation_script = dictionary['dom_script'] # .get_text()
    return div, script, dom_manipulation_script


@app.route('/')
def index():
    user = instagram.Profile('bryoh_15')
    follows_vs_following = return_ordered_div_elements(create_chart_elements('Followers vs Following', ['followers', 'following'], [user.followers, user.follows], "Pie"))
    example = return_ordered_div_elements(create_chart_elements('Example', ['followers', 'following'], [user.followers, user.follows], "Pie"))
    # example = return_ordered_div_elements(create_chart_elements('test', ["#E24736", "#FF9438", "#FFF249"], [5, 5.5, 10], "PolarArea"))
    return render_template('index_.html',
                           example=example,
                           follows_vs_following=follows_vs_following)


if __name__ == '__main__':
    app.run()
