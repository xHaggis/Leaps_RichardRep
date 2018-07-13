import cozmo
import Agent
import time
import asyncio

global robot
global homeBase
global enemyBase
global assignedNumber
global enemyNumber

homeBase = 99
enemyBase = 98
assignedNumber = 1
enemyNumber = 2
robot = cozmo.robot.Robot

'''''''''
def ArenaCode(evt, **kwargs):
    look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)

    # try to find a block
    cube = None

    try:
        cube = robot.world.wait_for_observed_light_cube(timeout=30)
        print("Found cube", cube)

    except asyncio.TimeoutError:
        print("Didn't find a cube :-(")

    finally:
        # whether we find it or not, we want to stop the behavior
        look_around.stop()

    if cube is None:
        robot.play_anim_trigger(cozmo.anim.Triggers.MajorFail)
        return

    if cube is not None:
        robot.pickup_object(self,)

    print("Yay, found cube")

    robot.turn_in_place(degrees(90)).wait_for_completed()

    action = robot.place_object_on_ground_here(cube)
    print("got action", action)
    result = action.wait_for_completed(timeout=30)
    print("got action result", result)
''''

def ArenaCode(evt, **kwargs):
    gameInProgress = True

    while gameInProgress = True:
        

    if homeBase = 98:

    robot.drive_wheels(50)



cozmo.run_program(ArenaCode)


