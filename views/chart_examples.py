'''
chart arguments dictionary

ret = {'name': None, 'chart_type': None, 'labels': None}

'''
import chartjs
from pprint import pprint as pp
from bs4 import BeautifulSoup

def example(args_dict=None):
    ''' TODO: Modify this so that is accepts a dictionary with 4 keys '''
    # Make a pie chart
    mychart = chartjs.chart("Sample pie chart", "PolarArea")  # args_dict['name'] args_dict['chart_type']
    # Add labels, colors, highlights and data values
    mychart.set_labels(["Apple", "Orange", "Banana"])  # args_dict['labels']
    mychart.set_colors(["#E24736", "#FF9438", "#FFF249"])  
    mychart.set_highlights(["#E07369", "#FFAC68", "#FFF293"])
    mychart.add_dataset([5,2.3,10])  # args_dict['dataset']
    return mychart.make_chart()


def chart_constructor(args_dict):
    name= args_dict['name']
    labels= args_dict['labels']
    dataset = args_dict['dataset']
    chart_type = args_dict['chart_type']
    chart_obj = chartjs.chart(name, chart_type)
    chart_obj.set_labels(labels)
    chart_obj.set_colors(["#E24736", "#FF9438", "#FFF249"])  
    chart_obj.set_highlights(["#E07369", "#FFAC68", "#FFF293"])
    chart_obj.add_dataset(dataset)
    return chart_obj.make_chart()


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



def random_colour():
    ''' generates a random colour '''
    # TODO: Expand this function so that it generates a random colour from a range
    pass


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
    import pdb; pdb.set_trace()
    elements = create_chart_elements('test', ["#E24736", "#FF9438", "#FFF249"], [5, 5.5, 10], "PolarArea")
    pp(elements)
