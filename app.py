from flask_socketio import SocketIO
from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)

def randomNumberGenerator():
    socketio.emit('my event', str({'number': "hello"}), namespace='/test')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    randomNumberGenerator()
    print('Client connected')

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)