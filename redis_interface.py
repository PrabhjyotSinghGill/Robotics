import redis
import json

redis_interface=redis.Redis(host='192.168.10.117',port='6379')
def set_progress_text(x):
    try:
        redis_interface.hset('HVROBOTKEY',"TEXT",x)
    except:
        pass

def get_progress_text():
    try:
        status=redis_interface.hget("HVROBOTKEY","TEXT").decode("utf-8")
        if not status:
            return ""
        return status
    except:
        ""

def set_progress_cells(dict):
    try:
        redis_interface.set('HVROBODICT', json.dumps(dict))
    except:
        pass

def get_progress_cells():
    return json.loads(redis_interface.get('HVROBODICT').decode('utf-8'))







