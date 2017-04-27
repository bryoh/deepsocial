import deepsocial.views.chart_examples as fut

import re
chart_name = 'test'
chart_labels = 'blue', 'red', 'white'
chart_data_set = 12, 15, 200
chart_type = 'PolarArea'


def test_random_colour():
    rgbstring = re.compile(r'#[a-fA-F0-9]{6}$')
    ishexcolour =  lambda value: True if rgbstring.match(value) else False
    print('CHECK: Random generour is hex')
    assert ishexcolour(fut.random_colour()) == True, 'Default random generator is hex'
    print('CHECK: Colour generator is hex with range')
    assert ishexcolour(fut.random_colour(int_range=(10, 254))) == True, 'color generator is hex with range'
    print('CHECK: RGB values')
    assert ishexcolour(fut.random_colour('rgba')) == False, 'RGB'
    assert fut.random_colour(colour_typ='other') == None, 'Sanity check'




def test_create_arg_dic():
    ret = fut.create_arg_dic(chart_name, chart_labels, chart_data_set, chart_type)
    expected = 'name', 'labels', 'dataset', 'chart_type'
    ret_keys = ret.keys()
    print(list(ret.keys()))
    assert set(ret_keys) == set(expected), 'Expected list of keys is correct'
    assert len(ret_keys) == len(expected), 'Number of keys'


def test_create_chart_elements():
    ret = fut.create_chart_elements(chart_name, chart_labels, chart_data_set, chart_type)
    expected = 'canvas', 'body_script', 'dom_script'
    ret_keys = ret.keys()
    assert set(ret_keys) == set(expected), 'Keys'
    assert len(ret_keys) == len(expected), 'Number of keys'


