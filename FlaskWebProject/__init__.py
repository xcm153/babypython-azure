"""
The flask application package.
"""

from flask import Flask ,Blueprint
from flask import session
from flask_socketio import SocketIO, emit, join_room

socketio = SocketIO()

def create_app(debug=False):
    """Create an application."""

    main_blueprint = Blueprint('main', __name__)
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'


    app.register_blueprint(main_blueprint)
    socketio.init_app(app)

    return app
app=create_app(debug=True)




import FlaskWebProject.views


@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""

    join_room("")
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room='')


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""

    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room='')


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""

    leave_room('')
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room='')
