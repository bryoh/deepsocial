from flask import Flask, render_template
from views.chart_examples import create_chart_elements
from datacollection import instagram
import datetime
# from chart_examples import create_chart_elements
from pprint import pprint


app = Flask(__name__)

time_labels = "%d%b"


def return_ordered_div_elements(dictionary):
    """
    :param dictionary:
    :return: div, script, dom_manipulation script

    returns a list of div, script(with variables), script for dom-manipulation
    """
    div = dictionary['canvas']
    script = dictionary['body_script']# .get_text()  # remove the tags
    dom_manipulation_script = dictionary['dom_script'] # .get_text()
    return div, script.text, dom_manipulation_script.text


def created_time_vs_likes(obj):
    """returns a tuple of (created, likes) where both elements are lists """
    ret = {"Late_Night": 0, "Morning": 0, "Afternoon": 0, "Evening": 0, "Early_night": 0}

    for obj in obj.media_recent_obj_list:
        hour = datetime.datetime.strptime(obj.created_time, "%c").hour
        val = int(obj.likes)
        if hour <= 6: ret["Late_Night"] += val
        elif hour <= 12: ret["Morning"] += val
        elif hour <= 15: ret["Afternoon"] += val
        elif hour <= 18: ret["Evening"] += val
        else: ret["Early_night"] += val

    labels = ["Late_Night", "Morning", "Afternoon", "Evening", "Early_night"]
    values = [ret.get(labels[0]), ret.get(labels[1]), ret.get(labels[2]), ret.get(labels[3]), ret.get(labels[4])]
    print(labels)
    print(values)
    return labels, values


@app.route('/')
def index():
    user = instagram.Profile('bryoh_15')
    popular_times_data = created_time_vs_likes(user)
    follows_vs_following = return_ordered_div_elements(create_chart_elements('Followers vs Following', ['followers', 'following'], [user.followers, user.follows], "Pie"))
    example = return_ordered_div_elements(create_chart_elements('test', ["#E24736", "#FF9438", "#FFF249"], [5, 5.5, 10], "PolarArea"))
    growth = return_ordered_div_elements(create_chart_elements('Recent rate of Growth', user.created_times_fmt(time_labels), user.recent_likes_reversed(), 'Line'))
    popular_times = return_ordered_div_elements(create_chart_elements('Popular times', popular_times_data[0], popular_times_data[1], 'Radar'))
    return render_template('index_.html',
                           example=example,
                           follows_vs_following=follows_vs_following,
                           growth=growth,
                           popular_times=popular_times)


if __name__ == '__main__':
    app.run()
