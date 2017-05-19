from flask import Flask, render_template
from views.chart_examples import create_chart_elements
from datacollection import instagram
import datetime
from collections import Counter
# from chart_examples import create_chart_elements
from pprint import pprint


app = Flask(__name__)

time_labels = "%d%b"


def return_word_cloud(title, user, element_id):
    common_tags_dict = ''
    for k, v in user.common_tags_dict.items():
        common_tags_dict += '{text: "%s",weight: %s},' % (str(k), str(v))
    div = """
     <h2> %s </h2>
    <div id="%s" style="height: 200px; width:400px; "></div>
        """ %(title, element_id)

    script = """ $(function() { $("#%s").jQCloud([%s],{autoResize: true});
      });
    """ %(element_id, common_tags_dict)

    return div, script



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
    ret = {"00-06 am": 0, "6-12 noon": 0, "12-3pm": 0, "3-6pm": 0, "6-Midnight": 0}

    for obj in obj.media_recent_obj_list:
        hour = datetime.datetime.strptime(obj.created_time, "%c").hour
        val = int(obj.likes)
        if hour <= 6: ret["00-06 am"] += val
        elif hour <= 12: ret["6-12 noon"] += val
        elif hour <= 15: ret["12-3pm"] += val
        elif hour <= 18: ret["3-6pm"] += val
        else: ret["6-Midnight"] += val

    labels = ["00-06 am", "6-12 noon", "12-3pm", "3-6pm", "6-Midnight"]
    values = [ret.get(labels[0]), ret.get(labels[1]), ret.get(labels[2]), ret.get(labels[3]), ret.get(labels[4])]
    return labels, values


def created_day_vs_likes(obj):
    """returns a tuple of (created, likes) where both elements are lists """

    labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    ret = {}
    [ret.setdefault(label, 0) for label in labels]

    for obj in obj.media_recent_obj_list:
        posted_day = datetime.datetime.strptime(obj.created_time, "%c").strftime('%a')
        val = int(obj.likes)
        ret[posted_day] = ret.get(posted_day, 0) + val
    values = [ ret[label] for label in labels]
    return labels, values


@app.route('/')
def index():
    user = instagram.Profile('bryoh_15')
    popular_times_data = created_time_vs_likes(user)
    popular_days_data = created_day_vs_likes(user)
    follows_vs_following = return_ordered_div_elements(create_chart_elements('Followers vs Following', ['followers', 'following'], [user.followers, user.follows], "Pie"))
    example = return_ordered_div_elements(create_chart_elements('test', ["#E24736", "#FF9438", "#FFF249"], [5, 5.5, 10], "PolarArea"))
    growth = return_ordered_div_elements(create_chart_elements('Likes vs Time', user.created_times_fmt(time_labels), user.recent_likes_reversed(), 'Line'))
    comment_growth = return_ordered_div_elements(create_chart_elements('Comments vs Time', user.created_times_fmt(time_labels), user.recent_comment_count(), 'Line'))
    popular_times = return_ordered_div_elements(create_chart_elements('Popular times', popular_times_data[0], popular_times_data[1], 'Radar'))
    popular_days = return_ordered_div_elements(create_chart_elements('Popular Days', popular_days_data[0], popular_days_data[1], 'Radar'))
    common_tags = return_word_cloud('Most used hastags', user, 'myHashtags')
    return render_template('index_.html',
                           example=example,
                           follows_vs_following=follows_vs_following,
                           growth=growth,
                           comment_growth=comment_growth,
                           popular_times=popular_times,
                           popular_days=popular_days,
                           common_tags=common_tags)


if __name__ == '__main__':
    app.run()
