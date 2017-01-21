from flask import session, render_template, request
from FlaskWebProject import app



@app.route('/', methods=['GET'])
def index():

    name = request.args.get('name', 'none')

    session['name']=name

    return render_template('chat.html', name=name, room='')
