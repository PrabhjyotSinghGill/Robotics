from flask import Flask, render_template, abort, request,\
                    redirect, url_for, flash, send_file, jsonify
from redis_interface import set_progress_text, get_progress_text, set_progress_cells
#from xARMInstructions import robot_instructions
from multiprocessing import Process
from time import sleep
global app
app = Flask(__name__)

PROCESS_START_PROCESS = None


def set_state(cell11, cell12, cell13 , cell14):
    dict={}
    dict['cell11']=cell11
    dict['cell12']=cell12
    dict['cell13']=cell13
    dict['cell14']=cell14
    set_progress_cells(dict)

def dummy_robot():
    set_state('                    ', '                    ', '                    ', '                    ')
    set_state('TBD', 'TBD', 'TBD', 'TBD')
    sleep(1)
    set_state('Done','TBD','TBD','TBD')
    sleep(1)
    set_state('Done', 'Done', 'TBD', 'TBD')
    sleep(1)
    set_state('Done', 'Done', 'Done', 'TBD')
    sleep(1)
    set_state('Done', 'Done', 'Done', 'Done')
    return


def start_process():
    #robot_instructions()
    dummy_robot()
    return

@app.route('/startrobot/', methods=['GET'])
def set_automatic_operation():
    global PROCESS_START_PROCESS
    PROCESS_START_PROCESS = Process(target=start_process)
    PROCESS_START_PROCESS.start()

    return '', 204

@app.route('/haltrobot/', methods=['GET'])
def stop_automatic_operation():
    global PROCESS_START_PROCESS
    PROCESS_START_PROCESS.terminate()
    return '', 204





if __name__ == "__main__":
    set_state('                    ', '                    ', '                    ', '                    ')
    app.run(host='0.0.0.0', port='5002')
