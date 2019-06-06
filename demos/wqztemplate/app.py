from flask import Flask, render_template

app = Flask(__name__)

namelist = ['chengli', 'qizhi', 'zhangsan', 'wangqizhi']

name2 = 'wangqizhi'

user = {
    'username': 'Grey Li',
    'bio': 'A boy who loves movies and music.',
}
movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]

mylist = ['list01', 'list02']
mydic = {'name': 'dicname'}


@app.route('/')
def index():
    return render_template('index.html', movies=movies, name2=name2, mylist=mylist, mydic=mydic)


@app.template_global()
def test():
    return "method test!"
