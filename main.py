from sys import stdout
import logging
from redis_interface import set_progress_text, get_progress_text, get_progress_cells
logging.basicConfig(level=logging.ERROR, filename='error.log')
logger = logging.getLogger(__name__)
import logging
from flask import Flask, render_template, Response, request, session
from flask_socketio import SocketIO, emit
from time import sleep


clients=[]



PROCESS_START_PROCESS = None

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(stdout))
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
app.config['cors_allowed_origins'] = "*"
socketio = SocketIO(app)

#lock = multiprocessing.Lock()
FLAG_HOLDER = {}





def instantiate_flags():
    FLAG_HOLDER['mode'] = ""
    FLAG_HOLDER['manual_operation'] = ""
    FLAG_HOLDER['in_execution'] = 0
    FLAG_HOLDER['img1'] = "static/assets/progress_icons/start.png"
    FLAG_HOLDER['img2'] = "static/assets/progress_icons/start.png"
    FLAG_HOLDER['img3'] = "static/assets/progress_icons/start.png"
    FLAG_HOLDER['img4'] = "static/assets/progress_icons/start.png"


def broadcast_progress():
    dict=get_progress_cells()
    socketio.emit('update-progress-event',{'cell11': dict['cell11'],'cell12': dict['cell12'],'cell13': dict['cell13'],'cell14': dict['cell14']})

@socketio.on('request_progress')
def request_progress():
    broadcast_progress()


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('startPage.html')

@app.route('/setmode/', methods=['GET'])
def set_mode():
    fetched_mode = str(request.args.get('m'))
    FLAG_HOLDER['mode'] = fetched_mode
    return '', 204


@app.route('/setmanualoperation/', methods=['GET'])
def set_manual_operation():
    fetched_operation = str(request.args.get('o'))
    FLAG_HOLDER['manual_operation'] = fetched_operation
    return '', 204




@app.route('/startmanual/', methods=['GET'])
def start_execution_manual():
    return '', 204







if __name__ == '__main__':
    instantiate_flags()
    socketio.run(app, host="0.0.0.0", port="5001")