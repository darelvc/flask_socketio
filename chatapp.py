from flask import render_template, Flask
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'klfdjlgrksalfdsfsd'
socketio = SocketIO(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/chat.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class History(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    message = db.Column('message', db.String(500))
    user = db.Column('user', db.String(80))


@app.route('/')
def index():
    db.create_all()
    messages = History.query.all()
    return render_template('index.html', messages=messages)


def messageRecived():
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json_data):
    print('received something: ', str(json_data))
    if 'msg' in json_data.keys():
        message = History(message=json_data['msg'], user=json_data['user'])
        db.session.add(message)
        db.session.commit()
    socketio.emit('my response', json_data, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug = True)