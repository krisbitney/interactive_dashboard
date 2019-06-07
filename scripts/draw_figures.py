import scripts.get_data as gd
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """


    # first plot -> gdp over time
    api_request_json = gd.request_wb_data('NY.GDP.MKTP.KD')
    data = gd.clean_json_data(api_request_json)
    graph_one = []
    for country in data.keys():
        graph_one.append(
            go.Scatter(x=data[country][0], y=data[country][1], mode='lines', name=country)
        )
    layout_one = dict(title='GDP over Time (2010 dollars)', xaxis=dict(title='Year'))

    # second plot -> gdp growth over time
    api_request_json = gd.request_wb_data('NY.GDP.MKTP.KD.ZG')
    data = gd.clean_json_data(api_request_json)
    graph_two = []
    for country in data.keys():
        graph_two.append(
            go.Scatter(x=data[country][0], y=data[country][1], mode='lines', name=country)
        )
    layout_two = dict(title='GDP Growth over Time', xaxis=dict(title='Year'), yaxis=dict(title='%'))

    # remaining plots not real
    graph_three = []
    graph_three.append(
      go.Scatter(x=[5, 4, 3, 2, 1, 0], y=[0, 2, 4, 6, 8, 10], mode='lines')
    )

    layout_three = dict(title = 'Chart Three',
                xaxis = dict(title = 'x-axis label'),
                yaxis = dict(title = 'y-axis label')
                       )

    graph_four = []
    graph_four.append(
      go.Scatter(x=[20, 40, 60, 80], y=[10, 20, 30, 40], mode='markers')
    )

    layout_four = dict(title = 'Chart Four',
                xaxis = dict(title = 'x-axis label'),
                yaxis = dict(title = 'y-axis label'),
                )


    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures