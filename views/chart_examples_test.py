import deepsocial.views.chart_examples as fut


def test_random_colour():
    given = 'blah'
    expected = 'blah'
    assert fut.random_colour() == expected 
