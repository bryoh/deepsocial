'''
chart arguments dictionary

ret = {'name': None, 'chart_type': None, 'labels': None}

'''
import chartjs
from pprint import pprint as pp
from bs4 import BeautifulSoup
from random import randint


def example():
    ''' TODO: Modify this so that is accepts a dictionary with 4 keys '''
    # Make a pie chart
    mychart = chartjs.chart("Sample pie chart", "PolarArea")  # args_dict['name'] args_dict['chart_type']
    # Add labels, colors, highlights and data values
    mychart.set_labels(["Apple", "Orange", "Banana"])  # args_dict['labels']
    mychart.set_colors(["#E24736", "#FF9438", "#FFF249"])  
    mychart.set_highlights(["#E07369", "#FFAC68", "#FFF293"])
    mychart.add_dataset([5,2.3,10])  # args_dict['dataset']
    return mychart.make_chart()


class ChartJs(chartjs.chart):
    def my_make_chart_onload(self):
        output = """var ctx{0} = document.getElementById("{0}").getContext("{1}");
                    var mychart{0} = new Chart(ctx{0}).{2}(chart_data{0}, {{responsive: true, barValueSpacing: {3}, scaleShowGridLines: {4}, scaleBeginAtZero: {5}}});""".format(
            str(self.canvas),
            str(self.context),
            str(self.ctype),
            str(self.barValueSpacing),
            str(self.scaleShowGridLines).lower(),
            str(self.scaleBeginAtZero).lower()
        )
        return output

    def my_make_chart(self):

        output = self.make_chart_canvas()

        output += """			<script>

                """
        output += self.my_make_chart_onload()
        output += """
            </script>
"""
        return output


def chart_constructor(args_dict):
    """
    Creates a chartjs object
    :param args_dict:
    :return: obj
    """
    name = args_dict['name']
    name = str(name).replace(' ','')
    labels = args_dict['labels']
    data_set = args_dict['dataset']
    chart_type = args_dict['chart_type']
    chart_obj = ChartJs(name, chart_type)
    chart_obj.set_labels(labels)
    chart_obj.canvas = name
    list_of_colors = [random_colour() for i in range(len(labels))]
    list_of_highlights = [random_colour() for i in range(len(labels))]
    chart_obj.set_colors(list_of_colors)
    chart_obj.set_highlights(list_of_highlights)
    chart_obj.add_dataset(data_set)
    return chart_obj.my_make_chart()


def create_soup(html_str):
    ''' accepts html text and returns a a bs4 soup object for interaction '''
    return BeautifulSoup(html_str, 'html.parser')


def get_DOM_tags(soup, tags):
    ''' returns a list of tag objects from a bs4 object '''
    all_tags = soup.find_all()
    return [item for item in all_tags if getattr(item, 'name') in tags]


def return_chartjs_dic(list_of_html_tags):
    ''' returns a dictionary of 3 keys which are canvas, fuction script(with data set) and function script for dom Manipulation '''
    ret = {'canvas': list_of_html_tags[0], 'body_script': list_of_html_tags[1], 'dom_script': list_of_html_tags[2]}
    return ret


def random_colour(colour_typ='hex', int_range=None):
    ''' generates a random colour '''
    if int_range is None:
        int_range = 0, 255

    if colour_typ == "hex":
        integer_values = lambda: randint(int_range[0], int_range[1])
        return '#%02X%02X%02X' % (integer_values(), integer_values(), integer_values())
    if colour_typ == "rgba":
        return "rgba({},{},{},{})".format(randint(100, 200), randint(120, 200), randint(100, 200),randint(150, 200))


def create_arg_dic(chart_name, chart_labels, chart_data_set, chart_type):
    ''' create a dictionary to use as the argument for the chart constructor '''
    return {'name': chart_name, 'labels': chart_labels, 'dataset':
           chart_data_set, 'chart_type': chart_type}


def create_chart_elements(chart_name, chart_labels, chart_data_set, chart_type):
    ''' main function that combines all the tools into one '''
    args_dict = create_arg_dic(chart_name, chart_labels, chart_data_set, chart_type)
    html_str = chart_constructor(args_dict)
    soup = create_soup(html_str)
    list_of_html_tags = get_DOM_tags(soup, ['canvas', 'script'])
    return return_chartjs_dic(list_of_html_tags)


if __name__ == '__main__':
    ret= example()
    elements = create_chart_elements('test', ["#E24736", "#FF9438", "#FFF249"], [5, 5.5, 10], "PolarArea")
    pp(elements)
