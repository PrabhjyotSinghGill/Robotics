#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2021, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

"""
# Notice
#   1. Changes to this file on Studio will not be preserved
#   2. The next conversion will overwrite the file with the same name
"""
import sys
import math
import time
import datetime
import random
import traceback
import threading

"""
# xArm-Python-SDK: https://github.com/xArm-Developer/xArm-Python-SDK
# git clone git@github.com:xArm-Developer/xArm-Python-SDK.git
# cd xArm-Python-SDK
# python setup.py install
"""
try:
    from xarm.tools import utils
except:
    pass
from xarm import version
from xarm.wrapper import XArmAPI
from redis_interface import set_progress_cells

def set_state(cell11, cell12, cell13 , cell14):
    dict={}
    dict['cell11']=cell11
    dict['cell12']=cell12
    dict['cell13']=cell13
    dict['cell14']=cell14
    set_progress_cells(dict)

def pprint(*args, **kwargs):
    try:
        stack_tuple = traceback.extract_stack(limit=2)[0]
        print('[{}][{}] {}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), stack_tuple[1], ' '.join(map(str, args))))
    except:
        print(*args, **kwargs)

pprint('xArm-Python-SDK Version:{}'.format(version.__version__))

arm = XArmAPI('192.168.1.205')
arm.clean_warn()
arm.clean_error()
arm.motion_enable(True)
arm.set_mode(0)
arm.set_state(0)
time.sleep(1)

variables = {}
params = {'speed': 100, 'acc': 2000, 'angle_speed': 20, 'angle_acc': 500, 'events': {}, 'variables': variables, 'callback_in_thread': True, 'quit': False}


# Register error/warn changed callback
def error_warn_change_callback(data):
    if data and data['error_code'] != 0:
        params['quit'] = True
        pprint('err={}, quit'.format(data['error_code']))
        arm.release_error_warn_changed_callback(error_warn_change_callback)
arm.register_error_warn_changed_callback(error_warn_change_callback)


# Register state changed callback
def state_changed_callback(data):
    if data and data['state'] == 4:
        if arm.version_number[0] > 1 or (arm.version_number[0] == 1 and arm.version_number[1] > 1):
            params['quit'] = True
            pprint('state=4, quit')
            arm.release_state_changed_callback(state_changed_callback)
arm.register_state_changed_callback(state_changed_callback)


# Register counter value changed callback
if hasattr(arm, 'register_count_changed_callback'):
    def count_changed_callback(data):
        if not params['quit']:
            pprint('counter val: {}'.format(data['count']))
    arm.register_count_changed_callback(count_changed_callback)


# Register connect changed callback
def connect_changed_callback(data):
    if data and not data['connected']:
        params['quit'] = True
        pprint('disconnect, connected={}, reported={}, quit'.format(data['connected'], data['reported']))
        arm.release_connect_changed_callback(error_warn_change_callback)
arm.register_connect_changed_callback(connect_changed_callback)

def robot_instructions():
    params['quit']=False
    set_progress_cells('                    ','                    ','                    ','                    ')
    # parts insertion from hanger starts
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[207.1, 0.0, 403.5, 180.0, -0.1, 0.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[207.1, 333.2, 403.5, 180.0, -0.1, 0.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[65.2, 333.2, 403.5, 180.0, -0.1, 0.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[65.2, 333.2, 403.5, 180.0, -0.1, 90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[65.2, 333.2, 403.5, 180.0, -90.0, 90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[124.6, 333.2, 160.8, 4.7, -90.0, -94.7], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[117.6, 399.3, 150.6, -16.6, -90.0, -73.4], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[117.6, 415.1, 148.6, -21.6, -90.0, -68.4], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_gripper_position(100, wait=True, speed=5000, auto_enable=True)
        if code != 0:
            params['quit'] = True
            pprint('set_gripper_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[117.6, 415.1, 143.5, -21.6, -90.0, -68.4], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[117.6, 290.2, 143.5, -21.6, -90.0, -68.4], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[117.6, 290.2, 400.0, 158.4, -90.0, 111.6], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[117.6, 290.2, 400.0, 180.0, -0.1, 90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[343.3, 290.2, 400.0, 180.0, -0.1, 0.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[343.3, 290.2, 400.0, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[302.5, 247.4, 322.9, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[287.1, 256.8, 298.7, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[287.1, 257.8, 296.7, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_gripper_position(500, wait=True, speed=5000, auto_enable=True)
        if code != 0:
            params['quit'] = True
            pprint('set_gripper_position, code={}'.format(code))
    set_state('Done','TBD','TBD','TBD')

    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[303.5, 242.4, 448.2, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[303.5, 242.4, 448.2, 180.0, -0.1, 0.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[303.5, 242.4, 448.2, 180.0, -0.1, 90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[140.1, 314.7, 448.2, 180.0, -0.1, 90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[140.1, 314.7, 448.2, 180.0, -90.0, 90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[25.7, 314.7, 217.3, 0.0, -90.0, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[27.2, 363.6, 171.9, -166.0, -90.0, 76.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[24.5, 406.1, 171.9, -168.3, -90.0, 78.3], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=True)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_gripper_position(80, wait=True, speed=5000, auto_enable=True)
        if code != 0:
            params['quit'] = True
            pprint('set_gripper_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[24.5, 406.1, 164.7, -166.0, -90.0, 76.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[24.5, 323.4, 164.7, -166.0, -90.0, 76.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[24.5, 323.4, 404.6, -166.0, -90.0, 76.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[253.1, 323.4, 404.6, 14.0, -90.0, -104.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[253.1, 323.4, 404.6, 180.0, -0.1, 90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    set_state('Done', 'Done', 'TBD', 'TBD')
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[316.1, 237.4, 404.6, 180.0, -0.1, 0.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[285.9, 215.8, 317.5, 180.0, -0.1, 0.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[283.9, 213.5, 303.4, 180.0, -0.1, 0.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_gripper_position(300, wait=True, speed=5000, auto_enable=True)
        if code != 0:
            params['quit'] = True
            pprint('set_gripper_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[301.5, 197.3, 457.6, 180.0, -0.1, 0.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=True)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_gripper_position(500, wait=True, speed=5000, auto_enable=True)
        if code != 0:
            params['quit'] = True
            pprint('set_gripper_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[207.1, 0.0, 621.0, 180.0, -0.1, 0.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if not params['quit']:
        time.sleep(10)
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[207.1, 0.0, 403.5, 180.0, -0.1, 0.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[207.1, -156.0, 378.9, 180.0, -0.1, 0.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[126.3, -156.0, 294.8, 180.0, -0.1, 0.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[115.8, -142.8, 273.5, 180.0, -0.1, 0.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[493.3, -142.8, 273.5, 180.0, -0.1, 0.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[493.3, -142.8, 414.8, 180.0, -0.1, 0.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[546.3, -142.8, 414.8, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[546.3, -142.8, 414.8, 195.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[613.5, -142.8, 308.4, -165.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    set_state('Done', 'Done', 'Done', 'TBD')
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[610.0, -175.0, 308.4, -165.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[612.8, -175.0, 257.4, -165.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_gripper_position(100, wait=True, speed=5000, auto_enable=True)
        if code != 0:
            params['quit'] = True
            pprint('set_gripper_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[612.8, -81.7, 257.4, -165.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_gripper_position(500, wait=True, speed=5000, auto_enable=True)
        if code != 0:
            params['quit'] = True
            pprint('set_gripper_position, code={}'.format(code))
    for i in range(int(1)):
        if params['quit']:
            break
        if arm.error_code == 0 and not params['quit']:
            code = arm.set_position(*[612.8, -175.0, 257.4, -165.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
            if code != 0:
                params['quit'] = True
                pprint('set_position, code={}'.format(code))
        if arm.error_code == 0 and not params['quit']:
            code = arm.set_gripper_position(100, wait=True, speed=5000, auto_enable=True)
            if code != 0:
                params['quit'] = True
                pprint('set_gripper_position, code={}'.format(code))
        if arm.error_code == 0 and not params['quit']:
            code = arm.set_position(*[612.8, -81.7, 257.4, -165.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
            if code != 0:
                params['quit'] = True
                pprint('set_position, code={}'.format(code))
        if arm.error_code == 0 and not params['quit']:
            code = arm.set_gripper_position(500, wait=True, speed=5000, auto_enable=True)
            if code != 0:
                params['quit'] = True
                pprint('set_gripper_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[612.8, -175.0, 257.4, -165.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_gripper_position(100, wait=True, speed=5000, auto_enable=True)
        if code != 0:
            params['quit'] = True
            pprint('set_gripper_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[612.8, -81.7, 257.4, -165.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if not params['quit']:
        time.sleep(10)
    for i in range(int(2)):
        if params['quit']:
            break
        if arm.error_code == 0 and not params['quit']:
            code = arm.set_position(*[612.8, -175.0, 257.4, -165.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
            if code != 0:
                params['quit'] = True
                pprint('set_position, code={}'.format(code))
        if arm.error_code == 0 and not params['quit']:
            code = arm.set_gripper_position(500, wait=True, speed=5000, auto_enable=True)
            if code != 0:
                params['quit'] = True
                pprint('set_gripper_position, code={}'.format(code))
        if arm.error_code == 0 and not params['quit']:
            code = arm.set_position(*[612.8, -81.7, 257.4, -165.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
            if code != 0:
                params['quit'] = True
                pprint('set_position, code={}'.format(code))
        if arm.error_code == 0 and not params['quit']:
            code = arm.set_gripper_position(100, wait=True, speed=5000, auto_enable=True)
            if code != 0:
                params['quit'] = True
                pprint('set_gripper_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[612.8, -167.6, 257.4, -165.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_gripper_position(500, wait=True, speed=5000, auto_enable=True)
        if code != 0:
            params['quit'] = True
            pprint('set_gripper_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[612.8, -167.6, 353.4, -165.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[612.8, -175.0, 426.4, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[551.3, -146.8, 308.9, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[545.3, -146.8, 277.7, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[164.0, -146.8, 277.7, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[187.8, -146.8, 277.7, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[187.8, -146.8, 516.3, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if not params['quit']:
        time.sleep(30)
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[271.9, -146.8, 358.0, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[283.8, -172.1, 311.5, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[287.4, -176.4, 254.3, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_gripper_position(50, wait=True, speed=5000, auto_enable=True)
        if code != 0:
            params['quit'] = True
            pprint('set_gripper_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[287.4, -86.3, 254.3, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_gripper_position(500, wait=True, speed=5000, auto_enable=True)
        if code != 0:
            params['quit'] = True
            pprint('set_gripper_position, code={}'.format(code))
    for i in range(int(2)):
        if params['quit']:
            break
        if arm.error_code == 0 and not params['quit']:
            code = arm.set_position(*[287.4, -185.8, 254.3, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
            if code != 0:
                params['quit'] = True
                pprint('set_position, code={}'.format(code))
        if arm.error_code == 0 and not params['quit']:
            code = arm.set_gripper_position(50, wait=True, speed=5000, auto_enable=True)
            if code != 0:
                params['quit'] = True
                pprint('set_gripper_position, code={}'.format(code))
        if arm.error_code == 0 and not params['quit']:
            code = arm.set_position(*[287.4, -85.6, 254.3, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
            if code != 0:
                params['quit'] = True
                pprint('set_position, code={}'.format(code))
        if arm.error_code == 0 and not params['quit']:
            code = arm.set_gripper_position(500, wait=True, speed=5000, auto_enable=True)
            if code != 0:
                params['quit'] = True
                pprint('set_gripper_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[287.4, -85.6, 380.5, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[283.8, -123.7, 530.8, 180.0, -0.1, -90.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    if arm.error_code == 0 and not params['quit']:
        code = arm.set_position(*[207.1, 0.0, 403.5, 180.0, -0.1, 0.0], speed=params['speed'], mvacc=params['acc'], radius=-1.0, wait=False)
        if code != 0:
            params['quit'] = True
            pprint('set_position, code={}'.format(code))
    set_state('Done', 'Done', 'Done', 'Done')

def release_robot():
    # release all event
    if hasattr(arm, 'release_count_changed_callback'):
        arm.release_count_changed_callback(count_changed_callback)
    arm.release_error_warn_changed_callback(state_changed_callback)
    arm.release_state_changed_callback(state_changed_callback)
    arm.release_connect_changed_callback(error_warn_change_callback)
