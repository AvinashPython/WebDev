from flask import Flask, url_for, render_template
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from MLmain import Lin_Reg
from content import Content

server = Flask(__name__)
content_dict = Content()
data1 = content_dict['Linear Regression'][0]
split = .2
data1_ans = Lin_Reg(split, data1[8],data1[9],data1[4],data1[5])
@server.route('/')
def home():
    return render_template('home.html', content_dict = content_dict)

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]
app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/',
    external_stylesheets=external_stylesheets
)

#app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

app.layout = html.Div(
    html.Div([
        html.Div(
            [
                html.H1(children='Machine Learning Visualization',
                        className='nine columns')
            ], className="row"
        ),

        html.Div(
            [
            html.Div([
                dcc.Graph(
                    id='example-graph',
                    figure={
                        'data': [
                            {'x': data1_ans[3], 'y': data1_ans[0][0], 'type': 'line', 'name': 'Grade 1'},
                            {'x': data1_ans[3], 'y': data1_ans[0][1], 'type': 'line', 'name': 'Grade 2'},
                            {'x': data1_ans[3], 'y': data1_ans[0][2], 'type': 'line', 'name': 'Study Hours'},
                            {'x': data1_ans[3], 'y': data1_ans[0][3], 'type': 'line', 'name': 'Health'},
                        ],
                        'layout': {
                            'title': 'Co-effecients Vs Data Points',
                            'xaxis' : dict(
                                title='Data points',
                                titlefont=dict(
                                family='Courier New, monospace',
                                size=20,
                                color='#7f7f7f'
                            )),
                            'yaxis' : dict(
                                title='Co-effecients',
                                titlefont=dict(
                                family='Helvetica, monospace',
                                size=20,
                                color='#7f7f7f'
                            ))
                        }
                    }
                )
                ], className= 'six columns'
                ),

            html.Div([
                dcc.Graph(
                    id='example-graph-2',
                    figure={
                        'data': [
                            {'y': [split], 'type': 'bar', 'name': 'Test set'},
                            {'y': [1-split], 'type': 'bar', 'name': 'Training set'},
                        ],
                        'layout': {
                            'title': 'Test vs Training split %'
                        }
                    }
                )
                ], className= 'six columns'
                )
            ], className="row"
        ),
        html.Div(
            [
            html.Div([
                dcc.Graph(
                    id='second row',
                    figure={
                        'data': [
                            {'x': data1_ans[3], 'y': data1_ans[2], 'type': 'line', 'name': 'Grade 1'}
                        ],
                        'layout': {
                            'title': 'error',
                            'xaxis' : dict(
                                title='Data points',
                                titlefont=dict(
                                family='Courier New, monospace',
                                size=20,
                                color='#7f7f7f'
                            )),
                            'yaxis' : dict(
                                title='Error',
                                titlefont=dict(
                                family='Helvetica, monospace',
                                size=20,
                                color='#7f7f7f'
                            ))
                        }
                    }
                )
                ], className= 'six columns'
                ),

            html.Div([
                dcc.Graph(
                    id='second row -2',
                    figure={
                        'data': [
                            {'x': data1_ans[3], 'y': data1_ans[1], 'type': 'Line'}
                        ],
                        'layout': {
                            'title': 'Accuracy'
                        }
                    }
                )
                ], className= 'six columns'
                )
            ], className="row"
        )
    ], className='eleven columns offset-by-one')
)

if __name__ == "__main__":
    server.run(debug=True)