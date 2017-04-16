import chartjs
from pprint import pprint as pp
from bs4 import BeautifulSoup

def chart_constructor(args_dict=None):
    ''' TODO: Modify this so that is accepts a dictionary with 4 keys '''
    # Make a pie chart
    mychart = chartjs.chart("Sample pie chart", "PolarArea")  # args_dict['name'] args_dict['chart_type']
    # Add labels, colors, highlights and data values
    mychart.set_labels(["Apple", "Orange", "Banana"])  # args_dict['labels']
    mychart.set_colors(["#E24736", "#FF9438", "#FFF249"])  
    mychart.set_highlights(["#E07369", "#FFAC68", "#FFF293"])
    mychart.add_dataset([5,2.3,10])  # args_dict['dataset']
    return mychart.make_chart()


def create_soup(html_str):
    ''' accepts html text and returns a a bs4 soup object for interaction '''
    return BeautifulSoup(html_str, 'html.parser')


def get_DOM_tags(soup, tags):
    ''' returns a list of tag objects from a bs4 object '''
    all_tags = soup.find_all()
    return [item for item in all_tags if getattr(item, 'name') in tags]



def return_chartjs_dic(list_of_html_tags):
    ''' returns a dictionary of 3 keys which are canvas, fuction script(with data set) and function script for dom Manipulation '''
    pass


def random_colour():
    ''' generates a random colour '''
    # TODO: Expand this function so that it generates a random colour from a range
    pass

def create_arg_dic(chart_name, chart_labels, chart_data_set, chart_type):
    ''' create a dictionary to use as the argument for the chart constructor '''
    pass # returns a dict


def create_chart_elements(chart_name, chart_labels, chart_data_set, chart_type):
    ''' main function that combines all the tools into one '''
    pass


if __name__ == '__main__':
    ret= chart_constructor()
    import pdb; pdb.set_trace()
    1+1
    soup = create_soup(ret)
    tags_list = get_DOM_tags(soup, ['canvas', 'script', 'script'])
    print(tags_list)

