
import time
import agent
import cozmo



def handle_object_moving_started(evt, **kw):
    # This will be called whenever an EvtObjectMovingStarted event is dispatched -
    # whenever we detect a cube starts moving (via an accelerometer in the cube)

    if evt.obj.object_id == 1 and evt.acceleration == 1:
        robot.drive_wheels(50,50)

    if evt.obj.object_id == 1 and evt.acceleration == -1:
        robot.drive_wheels(-50,-50)

    if evt.obj.object_id == 1 and evt.

    if evt.obj.object_id == 2 and evt.acceleration == 1:
        robot.drive_wheels(25,50)

    if evt.obj.object_id == 2 and evt.acceleration == -1:
        robot.drive_wheels(50,25)



def cozmo_program(robot: cozmo.robot.Robot):
    # Add event handlers that will be called for the corresponding event
    robot.add_event_handler(cozmo.objects.EvtObjectMovingStarted, handle_object_moving_started)



cozmo.robot.Robot.drive_off_charger_on_connect = False  # Cozmo can stay on his charger for this example
cozmo.run_program(cozmo_program)
