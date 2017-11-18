from flask import render_template, Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config['SECRET_KEY'] = 'klfdjlgrksalfdsfsd'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


def messageRecived():
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json_data):
    print('received something: ', str(json_data))
    socketio.emit('my response', json_data, callback=messageRecived)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug = True)
