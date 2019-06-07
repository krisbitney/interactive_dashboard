from myapp import app
import json
import plotly
from flask import render_template
from scripts.draw_figures import return_figures

@app.route('/')
@app.route('/index')
def index():
    ''' generate plot ids for the html id tag,
    encode plots as json objects,
    send ids and plots to front end
    '''
    figures = return_figures()
    ids = ['figure-{}'.format(i) for i in range(0, len(figures))]
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html', ids=ids, figuresJSON=figuresJSON)