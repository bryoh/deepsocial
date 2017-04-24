import deepsocial.views.chart_examples as fut

chart_name = 'test'
chart_labels = 'blue', 'red', 'white'
chart_data_set = 12, 15, 200
chart_type = 'PolarArea'


def test_random_colour():
    given = 'blah'
    expected = 'blah'
    assert fut.random_colour() == expected 


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


