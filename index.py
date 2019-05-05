# https://qiita.com/Gen6/items/949babb51d0cc000dcfb
from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hel3lo {{name}}</b>!', name=name)


run(host='localhost', port=8080)