import cozmo
import agent
import time

def cube_moved(evt):
    evt.






def ControlWhite1(evt, robot: cozmo.robot.Robot):
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)