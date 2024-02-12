from stressdetection.StressDetection import Stress
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--input', default=0,
                    help='Path to the video to be processed or webcam id (0 for example). Default value: 0.')
parser.add_argument('--rectangle', default=False, action='store_true',
                    help='Show the rectangle around the detected face. Default: False')
parser.add_argument('--landmarks', default=False, action='store_true',
                    help='Show the landmarks of the detected face. Default: False') 
parser.add_argument('--forehead', default=False, action='store_true',
                    help='Show the forehead in original color. Default: False')
parser.add_argument('--forehead_outline', default=True, action='store_true',
                    help='Draw a rectangle around the detected forehead. Default: True')
parser.add_argument('--fps', default=False, action='store_true',
                    help='Show the framerate. Default: False')

args = parser.parse_args()

stress = Stress()
stress.display_rectangle(args.rectangle)
stress.display_landmarks(args.landmarks)
stress.display_forehead(args.forehead)
stress.display_forehead_outline(args.forehead_outline)
stress.display_fps(args.fps)

stress.run(args.input)


from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from stressdetection.StressDetection import Stress
import argparse

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='http://127.0.0.1:5000')

# Define route to render canvas.html
@app.route('/')
def index():
    return render_template('canvas.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('start_stress_detection')
def start_stress_detection():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default=0, help='Path to the video to be processed or webcam id (0 for example). Default value: 0.')
    parser.add_argument('--rectangle', default=False, action='store_true', help='Show the rectangle around the detected face. Default: False')
    parser.add_argument('--landmarks', default=False, action='store_true', help='Show the landmarks of the detected face. Default: False') 
    parser.add_argument('--forehead', default=False, action='store_true', help='Show the forehead in original color. Default: False')
    parser.add_argument('--forehead_outline', default=True, action='store_true', help='Draw a rectangle around the detected forehead. Default: True')
    parser.add_argument('--fps', default=False, action='store_true', help='Show the framerate. Default: False')
    args = parser.parse_args()

    stress = Stress()
    stress.display_rectangle(args.rectangle)
    stress.display_landmarks(args.landmarks)
    stress.display_forehead(args.forehead)
    stress.display_forehead_outline(args.forehead_outline)
    stress.display_fps(args.fps)

    stress.run(args.input)

if __name__ == "__main__":
    stress_detection = Stress(socketio)
    socketio.run(app)
