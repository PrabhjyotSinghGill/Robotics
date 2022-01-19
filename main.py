from flask import Flask, render_template, abort, request,\
    redirect, url_for, flash, send_file, jsonify

global app
app = Flask(__name__)

FLAG_HOLDER = {}


def instantiate_flags():
    FLAG_HOLDER['mode'] = ""
    FLAG_HOLDER['manual_operation'] = ""
    FLAG_HOLDER['in_execution'] = 0


@app.route('/')
def home():
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


@app.route('/startauto/', methods=['GET'])
def start_execution_auto():
    return '', 204


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5001')
