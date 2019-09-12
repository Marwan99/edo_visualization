#! /usr/bin/env python
#rostopic pub /listener std_msgs/UInt32 3
import rospy
from edo_core_msgs.msg import CartesianPose
#from std_msgs.msg import UInt32
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
#app.config['DEBUG'] = True

socketio = SocketIO(app)

def ros_callback(msg):
    socketio.emit('newnumber', {'x': msg.x, 'y': msg.y, 'z': msg.z}, namespace='/test')
    #print(msg)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    print("---------------*Connected")
    rospy.init_node('viz', anonymous=True, disable_signals=True)
    rospy.Subscriber('/cartesian_pose', CartesianPose, ros_callback)
    rospy.loginfo("WebSocket started")
    '''
    while not rospy.is_shutdown():
        rospy.loginfo("2")
        rospy.spin()
        '''
    #return "1"

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

rospy.loginfo(str(__name__))

if __name__ == '__main__':
    socketio.run(app, host= '0.0.0.0')
