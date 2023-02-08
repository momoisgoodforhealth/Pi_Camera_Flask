#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request, send_from_directory
import cv2
import os

 # flip pi camera if upside down.

# App Globals (do not edit)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') #you can customze index.html here

def gen(camera):
    #get camera frame
    pi_camera = cv2.VideoCapture(camera)
    pi_camera.set(3,160)
    pi_camera.set(4,120)
    

    while(True):
        success, frame = pi_camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg',frame)
            frame = buffer.tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(0),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/video_feed1')
def video_feed1():
    return Response(gen(2),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/video_feed2')
def video_feed2():
    return Response(gen(4),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Take a photo when pressing camera button
@app.route('/picture')
def take_picture():
    pi_camera.take_picture()
    return "None"

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
