

import time

import cozmo
from cozmo.util import distance_mm, speed_mmps, degrees
g_robot = None



def handle_object_moving_started(evt, **kw):
    # This will be called whenever an EvtObjectMovingStarted event is dispatched -
    # whenever we detect a cube starts moving (via an accelerometer in the cube)
    print("Object %s started moving: acceleration=%s" %
          (evt.obj.object_id, evt.acceleration))
    if evt.obj.object_id == 1:
        if evt.acceleration.y >0:
            g_robot.drive_straight(distance_mm(50), speed_mmps(25)).wait_for_completed()

        if evt.acceleration.y <0:
            g_robot.drive_straight(distance_mm(-50), speed_mmps(-25)).wait_for_completed()

    if evt.obj.object_id == 2:
        if evt.acceleration.x >0:
            g_robot.turn_in_place(degrees(90)).wait_for_completed()

        if evt.acceleration.x <0:
            g_robot.turn_in_place(degrees(-90)).wait_for_completed()



def handle_object_tapped(evt, **kw):
    if evt.obj.object_id == 1:
        g_robot.move_lift(-5)

    if evt.obj.object_id == 2:
        g_robot.move_lift(5)



def handle_object_moving(evt, **kw):
    # This will be called whenever an EvtObjectMoving event is dispatched -
    # whenever we detect a cube is still moving a (via an accelerometer in the cube)
    print("Object %s is moving: acceleration=%s, duration=%.1f seconds" %
          (evt.obj.object_id, evt.acceleration, evt.move_duration))


def handle_object_moving_stopped(evt, **kw):
    # This will be called whenever an EvtObjectMovingStopped event is dispatched -
    # whenever we detect a cube stopped moving (via an accelerometer in the cube)
    print("Object %s stopped moving: duration=%.1f seconds" %
          (evt.obj.object_id, evt.move_duration))


def cozmo_program(robot: cozmo.robot.Robot):
    global g_robot
    g_robot = robot
    # Add event handlers that will be called for the corresponding event
    robot.add_event_handler(cozmo.objects.EvtObjectMovingStarted, handle_object_moving_started)
    robot.add_event_handler(cozmo.objects.EvtObjectMoving, handle_object_moving)
    robot.add_event_handler(cozmo.objects.EvtObjectMovingStopped, handle_object_moving_stopped)
    robot.add_event_handler(cozmo.objects.EvtObjectTapped, handle_object_tapped)

    # keep the program running until user closes / quits it
    print("Press CTRL-C to quit")
    while True:
        time.sleep(1.0)


cozmo.robot.Robot.drive_off_charger_on_connect = False  # Cozmo can stay on his charger for this example
cozmo.run_program(cozmo_program)



