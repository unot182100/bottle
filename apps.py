import os
from bottle import route, run
from bottle import get, post, request


@route('/', method='GET')
def input():
    input_txt = request.query.get('user')
    #GETで何も渡されていない時はinput_txtに何も入れない
    input_txt = "" if input_txt is None else input_txt
    return '''
    <form action="/" method="post">
            INPUT: <input name="input_txt" type="text" value="{input_txt}"/>
            <input value="echo" type="submit" />
        </form>
    '''.format(input_txt=input_txt)


@route('/', method='POST')
def do_echo():
    input_txt = request.forms.get('input_txt')
    return "{input_txt}".format(input_txt=input_txt)

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))