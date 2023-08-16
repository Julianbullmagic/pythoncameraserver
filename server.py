from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Serve the static HTML website
@app.route('/')
def index():
    return render_template('index.html')

# WebSocket event handler for image reception
@socketio.on('image')
def handle_image(data):
    # Broadcast the received image to all clients
    emit('image', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
